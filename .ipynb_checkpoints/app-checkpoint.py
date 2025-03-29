from flask import Flask, render_template, request, redirect
import pymongo
import csv
import os

# 1. Initialize Flask
app = Flask(__name__)

# 2. Configure MongoDB Client
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["survey_db"]  # your database name
collection = db["user_data"]  # your collection name

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Collect data from form
        age = request.form.get("age")
        gender = request.form.get("gender")
        total_income = request.form.get("total_income")
        
        # Checkboxes and their corresponding amounts
        expense_categories = {
            "utilities": request.form.get("utilities_amount") if request.form.get("utilities") else 0,
            "entertainment": request.form.get("entertainment_amount") if request.form.get("entertainment") else 0,
            "school_fees": request.form.get("school_fees_amount") if request.form.get("school_fees") else 0,
            "shopping": request.form.get("shopping_amount") if request.form.get("shopping") else 0,
            "healthcare": request.form.get("healthcare_amount") if request.form.get("healthcare") else 0
        }
        
        # Convert amounts to numeric values (optional)
        for key, val in expense_categories.items():
            expense_categories[key] = float(val) if val else 0.0
        
        # Insert data into MongoDB
        document = {
            "age": age,
            "gender": gender,
            "total_income": float(total_income) if total_income else 0.0,
            "expenses": expense_categories
        }
        collection.insert_one(document)
        
        return redirect("/")
    else:
        return render_template("index.html")

# Run Flask
if __name__ == "__main__":
    app.run(debug=True)
