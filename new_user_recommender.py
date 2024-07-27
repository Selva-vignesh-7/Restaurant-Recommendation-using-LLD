
import json
from pymongo import MongoClient
from settings import Settings
import re


def new_user_query(cusine,text1):
	BUSINESS_PROFILE = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.BUSINESS_COLLECTION] #collection name is b
	business_profile_cursor = BUSINESS_PROFILE.find()

	print("the cusine is:" , cusine)

	cusine_lower=cusine.lower()

	dict1={}
	dict2={}

	for i in business_profile_cursor:
		
		if((i["TEXT"].lower().find(cusine_lower)) != -1):
			
			if(i["STARS"]>=3):
				dict1.update({i["BUSINESS_ID"]:i["TEXT"]})

			elif(i["STARS"]<2):
				dict2.update({i["BUSINESS_ID"]:i["TEXT"]})

				
	emailid=text1


	return_string={
	"dict1": dict1,
	"dict2": dict2,
	"emailid":emailid
	}

	return return_string

