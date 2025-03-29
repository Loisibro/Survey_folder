import csv
import os

class User:
    def __init__(self, age, gender, total_income, expenses):
        self.age = age
        self.gender = gender
        self.total_income = total_income
        self.expenses = expenses
    
    def to_dict(self):
        """Return a dictionary representation of user data, useful for CSV writing."""
        return {
            "Age": self.age,
            "Gender": self.gender,
            "Total Income": self.total_income,
            "Utilities": self.expenses.get("utilities", 0),
            "Entertainment": self.expenses.get("entertainment", 0),
            "School Fees": self.expenses.get("school_fees", 0),
            "Shopping": self.expenses.get("shopping", 0),
            "Healthcare": self.expenses.get("healthcare", 0)
        }

    @staticmethod
    def write_to_csv(users, filename="user_data.csv"):
        """Write a list of User objects to a CSV file."""
        # Ensure the directory for the CSV file exists
        fieldnames = [
            "Age", 
            "Gender", 
            "Total Income", 
            "Utilities", 
            "Entertainment", 
            "School Fees", 
            "Shopping", 
            "Healthcare"
        ]
        
        with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for user in users:
                writer.writerow(user.to_dict())
