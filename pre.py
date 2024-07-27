import json
from pymongo import MongoClient
from settings import Settings
from predict import main as mn



USER_D = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.USER_STOP]#su
BUSINESS_D = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.BUSINESS_STOP]#sb



USER_PROFILE = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.USER_PROFILE]#up
BUSINESS_PROFILE = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.BUSINESS_PROFILE]#ub

user_profile_cursor=USER_D.find()
business_profile_cursor=BUSINESS_D.find()

for i in user_profile_cursor:
	USER_PROFILE.insert_one({
            "USER_ID":i["USER_ID"],
            "ENCRYPTED":str(mn(str(i["TEXT"])))
        })   

print("User profiles with their respective encoded values created which has their prefrences hidden in it")#,USER_PROFILE.count_documents({}))



for i in business_profile_cursor:
    BUSINESS_PROFILE.insert_one({
            "BUSINESS_ID":i["BUSINESS_ID"],
            "ENCRYPTED":str(mn(str(i["TEXT"])))
        })   

print("business profiles with their respective encoded values created which has their features hidden in it")#,BUSINESS_PROFILE.count_documents({}))

