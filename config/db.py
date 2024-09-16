from pymongo import MongoClient

MONGO_URI = "mongodb+srv://user1:fast123@cluster0.nccyp.mongodb.net"
conn = MongoClient(MONGO_URI)