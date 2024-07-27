
from predict import main as mn
import operator
import logging
import gensim
import pickle
import time
import nltk
from pymongo import MongoClient
from settings import Settings
#import pyLDAvis.gensim
import gensim.matutils
#from keras.models import load_model
#from keras.preprocessing.sequence import pad_sequences

import ast

import math
import scratch as sc

import predict as s
import os
import time
import json
# import string as str

from pymongo import MongoClient

from settings import Settings

#from app.py import text123


#===================flask imports============




#===========================================






def cosine_similarity(v1,v2):
    #"compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)



USER_PROFILE = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.USER_PROFILE]#ub
BUSINESS_PROFILE = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.BUSINESS_PROFILE]#up
BUSINESS_PROFILE1 = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.BUSINESS_COLLECTION]#b

USER_COMMENTS = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.USER_STOP]#su
BUSINESS_COMMENTS = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.BUSINESS_STOP]#sb
	

def calc_cos(user_id_ip):

	l=list(range(0,50))
	x={}
	y={}
	for i in l:
		x[i]=0
		y[i]=0

	test=user_id_ip
	d={}
	user_profile_cursor=USER_PROFILE.find()

	business_profile_cursor=BUSINESS_PROFILE.find()



	for i in user_profile_cursor:
		if (i["USER_ID"][0]==test):
			break

	print("test",test)
	print("USER_ID",i["USER_ID"])
	xx = dict(tuple(ast.literal_eval(i["ENCRYPTED"])))
	j=list(xx.keys())
	for loop in j:
		x[loop]=xx[loop]

	print("x" , x)
	return_string0=i["USER_ID"] #finds out the exact user being sent
	print("return_string0",return_string0)

	MY_LIST=[]
	
	for i in business_profile_cursor: 
		yy = dict(tuple(ast.literal_eval(i["ENCRYPTED"])))
		j=list(yy.keys())
		for loop in j:
			y[loop]=yy[loop]
		
		#print(i["USER_ID"])
		MY_LIST.append(cosine_similarity(x,y))
		d[i["BUSINESS_ID"]]=float(MY_LIST[-1])
		#print("This is the rating which the person could rate ",MY_LIST[-1])
		'''print("while Public rated this resturnt as ",s.run(bus_cur["BUSINESS_ID"]))'''
	
	for key, value in d.items():
	    print("restaurant:",key," recommendation:",(round((value*100),2)),"%")



	Keymax = max(d, key=d.get)
	Keymin = min(d, key=d.get)

	return_string1=""
	return_string2=""
	
	return_string1=str(Keymax)
	return_string1_1=str(round((d[Keymax])*100,2))+"%"

	return_string2=str(Keymin)
	return_string2_2=str(round((d[Keymin])*100,2))+"%"

	

	list1=[]
	list2=[]
	list3=[]


	USER_COMMENTS_CURSOR=USER_COMMENTS.find()
	print("\n\nUSER COMMENTS IS AS FOLLWS\n\n")
	for i in USER_COMMENTS_CURSOR:
		if (i["USER_ID"][0]==test):
			for j in (i["TEXT"]):
				list1.append(j)

	print("\n\nCOMMENTS ON BEST RECOMMENDED RESTAURANT IS AS FOLLOWS\n\n")

	

	BUSINESS_COMMENTS_CURSOR=BUSINESS_COMMENTS.find()
	for i in BUSINESS_COMMENTS_CURSOR:
		if(i["BUSINESS_ID"]==Keymax):
			for j in (i["TEXT"]):
				list2.append(j)
	

	print("\n\nCOMMENTS ON LEAST RECOMMENDED RESTAURANT IS AS FOLLOWS\n\n")


	BUSINESS_COMMENTS_CURSOR=BUSINESS_COMMENTS.find()
	for i in BUSINESS_COMMENTS_CURSOR:
		if(i["BUSINESS_ID"]==Keymin):
			for j in (i["TEXT"]):
				list3.append(j)

	return_string ={
	'return_string0' : return_string0,
	'return_string1' : return_string1,
	'return_string1_1':return_string1_1,
	'return_string2' : return_string2,
	'return_string2_2':return_string2_2,
	'list1' : list1,
	'list2' : list2,
	'list3' :list3
	}
	return return_string
	#return ("The least recommended restaurant is: {} {}".format(Keymin,d[Keymin]))
	'''
	print(BUSINESS_COMMENTS.find_one())

	for i in BUSINESS_COMMENTS_CURSOR:

		if ((i["BUSINESS_ID"][1])==Keymax):
			for j in (i["TEXT"]):
				print(j,)'''