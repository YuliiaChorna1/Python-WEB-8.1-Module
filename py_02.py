# Отримання документів

from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://yulichorna:LDMvypq6rAV4U37m@cluster0.iroiinp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    server_api=ServerApi('1')
)

db = client.book

result = db.cats.find_one({"_id": ObjectId("662cf49dd7c073b373d9b13a")})
print(result)
print("------------------------------------")

# Отримати декілька документів — метод find:

result2 = db.cats.find({})
for el in result2:
    print(el)


