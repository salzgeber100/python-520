
import pymongo

client = pymongo.MongoClient()
db = client.projeto

# collections
users = db.users