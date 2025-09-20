
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb://tusar_db:Admin1234@cluster0-shard-00-00.diyiptb.mongodb.net:27017,cluster0-shard-00-01.diyiptb.mongodb.net:27017,cluster0-shard-00-02.diyiptb.mongodb.net:27017/?ssl=true&replicaSet=atlas-diyiptb-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)