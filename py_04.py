# Видалення документів

from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://yulichorna:LDMvypq6rAV4U37m@cluster0.iroiinp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    server_api=ServerApi('1')
)

db = client.book

db.cats.delete_one({"name": "Lama"})
db.cats.delete_one({"name": "Liza"})
result = db.cats.find_one({"name": "Lama"})
result2 = db.cats.find_one({"name": "Lama"})
print(result, result2)

