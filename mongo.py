import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# Create DB
mydb = myclient["mydatabase"]

# List of DBs
print(myclient.list_database_names())

# Create Collection
mycol = mydb["customers"]

# List of Collections
print(mydb.list_collection_names())

"""Using DB"""
db = settings.MONGO_CLIENT.user.chats

db =  pymongo.MongoClient(MONGO_CONNECTION_STR).db_name.collection_name
"""Adding One Record in DB"""
post = {"channel_id": 1,
"author_id": 2,
"text": "Hi!"}
query = db.insert_one(post)


"""Adding Many Record in DB"""
query = db.insert_many([{"channel_id": 1,
		"author_id": 4,
        "text": "Hey Buddy!"},{"channel_id": 1,
		"author_id": 2,
        "text": "How Are you?"},{"channel_id": 1,
		"author_id": 4,
        "text": "I'm good!"}])		

# Fetch and Print Item from to Table
for post in client.user.chats.find():
	pprint.pprint(post)
		
# Fetch Data by passing a key
result = db.find({"channel_id":1})

# Sort in Asc order
result = db.find({"channel_id":1}).sort("_id")	

# Sort in Desc Order
result = db.find({"channel_id":1}).sort("_id",-1)

# Sort in Desc Order and limit 
result = db.find({"channel_id":1}).sort("_id",-1).limit(3)
data = json.loads(dumps(result))

# Deleting a record
db.delete_one({"channel_id":1})

# Deleting Multiple records
db.delete_many({"channel_id":1}) 
db.delete_many({ "address": {"$regex": "^S"} })

# Deleting all records
db.delete_many({})
