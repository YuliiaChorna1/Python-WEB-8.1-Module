import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.environ['DB_LOCAL_URI'])

# client.drop_database("main_db")
collection = client.main_db.users

database = client.main_db
collection.insert_one(...)
database.users.insert_one(
    {"name": "Dima", "positions": ["Engineer", "Lecturer"]}
)

print("---------------------------------------------")

# res = database.users.find({}, {"_id": 0, "positions": 0}) # prints only name
res = database.users.find({}, {"_id": 0})
for val in res:
    print(val)
    print(val["name"])
