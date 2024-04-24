from pymongo import MongoClient
import json
import time

def store_in_mongodb(data):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['streaming_data_db']
    collection = db['streaming_data_collection']
    
    try:
        # Attempt to insert the data into MongoDB
        collection.insert_one(data)
        print('Data Stored in MongoDB successfully')
    except Exception as e:
        # Print an error message if insertion fails
        print('Failed to store data in MongoDB:', str(e))

# Test MongoDB connection
try:
    client = MongoClient('mongodb://localhost:27017/')
    db = client.admin.command('ping')  # Ping the MongoDB server to check if it's reachable
    print('Connected to MongoDB successfully')
except Exception as e:
    print('Failed to connect to MongoDB:', str(e))

# Infinite loop to continuously send data to MongoDB
while True:
    # Load preprocessed data from JSON file
    with open('preprocessed_data.json', 'r') as f:
        preprocessed_data = json.load(f)
    
    # Store preprocessed data in MongoDB
    store_in_mongodb(preprocessed_data)
    
    # Add a delay before the next iteration to avoid consuming excessive CPU resources
    time.sleep(1)  # Adjust the sleep duration as needed

