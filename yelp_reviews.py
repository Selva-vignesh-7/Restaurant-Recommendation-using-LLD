import json
from pymongo import MongoClient
from settings import Settings



dataset_file = Settings.DATASET_FILE
USER_PROFILE = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.USER_COLLECTION] # collection name is u  
BUSINESS_PROFILE = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.BUSINESS_COLLECTION] #collection name is b



reviewsByUser = {}
with open(dataset_file) as dataset:
    count = sum(1 for line in dataset)

with open(dataset_file) as dataset:
    next(dataset)
    for line in dataset:
        try:
            data = json.loads(line)
        except ValueError:
            print('Oops!')
        # if data["type"] == "review":
        user_id=data["user_id"],
        text=data["text"]
        USER_PROFILE.insert_one({
            "USER_ID": data["user_id"],
            "TEXT": data["text"],
            "STARS":data["stars"]
        })
        if user_id not in reviewsByUser:
            reviewsByUser[user_id] = []


        reviewsByUser[user_id].append(text)
        #print(user_id)


         # if loop to categorise the review
#print("user profiles created\n",len(reviewsByUser))
#Call len(*args)  to return its length, which is the number of unique values
#this creates the number of unique users i.e(unique user_ids)
reviewsByBusiness = {}
with open(dataset_file) as dataset:
    next(dataset)
    for line in dataset:
        try:
            data = json.loads(line)
        except ValueError:
            print('Oops!')
        # if data["type"] == "review":
        business_id = data["business_id"]
        text = data["text"]
        BUSINESS_PROFILE.insert_one({
            "BUSINESS_ID": data["business_id"],
            "TEXT": data["text"],
            "STARS":data["stars"]
        })
        if business_id not in reviewsByBusiness:
            reviewsByBusiness[business_id] = []
        reviewsByBusiness[business_id].append(text) # if loop to categorise the review
#print("business profiles created \n",len(reviewsByBusiness)) 
#this creates the number of unique businesses i.e(unique business_ids)


#By the end of this file a databse named usr and collections named b for business and u for users is created with all the revies stored in it

 

