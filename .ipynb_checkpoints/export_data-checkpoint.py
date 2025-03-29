import pymongo
from user_class import User

def export_data_to_csv():
    # Connect to Mongo
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["survey_db"]
    collection = db["user_data"]

    # Fetch all documents
    docs = list(collection.find())
    
    # Convert each document to a User object
    users = []
    for doc in docs:
        age = doc.get("age")
        gender = doc.get("gender")
        total_income = doc.get("total_income")
        expenses = doc.get("expenses", {})
        
        user_obj = User(age, gender, total_income, expenses)
        users.append(user_obj)
    
    # Write to CSV
    User.write_to_csv(users, filename="user_data.csv")

if __name__ == "__main__":
    export_data_to_csv()
    print("Data exported to user_data.csv")
