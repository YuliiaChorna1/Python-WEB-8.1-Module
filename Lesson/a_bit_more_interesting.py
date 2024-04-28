import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.environ['DB_LOCAL_URI'])

# database = client.main_db # changed to:
collection = client.main_db.users

collection.insert_one(
    {
        "name": "Antony",
        "positions": ["Engineer", "Lecturer"],
        "best_friend": {"name": "Josh"},
        "friends": [{"name": "Josh"}, {"name": "Bob"}]
    }
)

res = collection.find_one({"best_friend.name": "Josh"})
print(res)

print("---------------------------------------------")

res = collection.find_one({"friends": {"$elemMatch": {"name": "Bob"}}})
print(res)

print("---------------------------------------------")

collection.insert_one(
    {
        "name": "Rob",
        "age": 28
    }
)

res = collection.find({"age": {"$gt": 20}}) # gte;lte;gt;lt;eq
for val in res:
    print(val)

print("---------------------------------------------")

res = collection.find({}).skip(2) # skip first 2 results
for val in res:
    print(val)

print("---------------------------------------------")

res = collection.find({}).limit(1)
for val in res:
    print(val)

print("---------------------------------------------")

res = collection.find({}).sort({"name": -1}).skip(3).limit(2) # -1 means descending
for val in res:
    print(val)

print("---------------------------------------------")

res = collection.count_documents({})
print(res)
