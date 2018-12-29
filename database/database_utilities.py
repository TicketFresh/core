from pymongo import MongoClient, InsertOne

if __name__ == "__main__":
    client = MongoClient('localhost', 27017)
    mdb = client["contacts"]  # database being used
    mdb_collection = mdb["customer"]  # collection being created
    test_user = {
    "first_name": "john",
    "last_name": "doe",
    "company": "John Deer Tractors"
     }
    mdb.mdb_collection.InsertOne(test_user)