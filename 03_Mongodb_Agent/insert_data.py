from pymongo import MongoClient
from datetime import datetime


# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client["student_records"]



# students data
students = [
    {
        "name": "Alice Johnson",
        "student_id": "20231230",
        "department": "Computer Science",
        "cgpa": 3.82,
        "graduation_year": 2024
    },
    {
        "name": "Bob Smith",
        "student_id": "20231231",
        "department": "Electrical Engineering",
        "cgpa": 3.55,
        "graduation_year": 2023
    },
    {
        "name": "Clara Lee",
        "student_id": "20231232",
        "department": "Mechanical Engineering",
        "cgpa": 3.91,
        "graduation_year": 2025
    },
    {
        "name": "David Kim",
        "student_id": "20231233",
        "department": "Computer Science",
        "cgpa": 3.67,
        "graduation_year": 2024
    },
    {
        "name": "Eva Martinez",
        "student_id": "20231234",
        "department": "CSE",
        "cgpa": 2.48,
        "graduation_year": 2025
    },
    {
        "name": "Farhan Ahmed",
        "student_id": "20231235",
        "department": "Data Science",
        "cgpa": 3.88,
        "graduation_year": 2025
    },
    {
        "name": "Grace Liu",
        "student_id": "20231236",
        "department": "Physics",
        "cgpa": 3.6,
        "graduation_year": 2024
    },
    {
        "name": "Hassan Chowdhury",
        "student_id": "20231237",
        "department": "CSE",
        "cgpa": 3.95,
        "graduation_year": 2025
    },
    {
        "name": "Isabella Tan",
        "student_id": "20231238",
        "department": "Information Technology",
        "cgpa": 1.85,
        "graduation_year": 2023
    },
    {
        "name": "James Thompson",
        "student_id": "20231239",
        "department": "Civil Engineering",
        "cgpa": 3.2,
        "graduation_year": 2024
    }
]


# Insert into collections
db.students.insert_many(students)

print("Data inserted successfully.")
