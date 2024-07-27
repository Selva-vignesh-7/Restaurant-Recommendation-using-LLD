


from predict import main as mn
import operator
import logging
import gensim
import pickle
import time
import nltk
from gensim import corpora
from gensim.corpora import BleiCorpus
from gensim.models import LdaModel
from pymongo import MongoClient
from settings import Settings
#import pyLDAvis.gensim
import gensim.matutils
#from keras.models import load_model
#from keras.preprocessing.sequence import pad_sequences

import ast

import math


import os
import time
import json
# import string as str

from pymongo import MongoClient

from settings import Settings

BUSINESS_D = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.BUSINESS_COLLECTION]
business_profile_cursor=BUSINESS_D.find()
class avg():
	def run(self, id):
		stars=0
		x=0

		for i in business_profile_cursor:
			if(i["BUSINESS_ID"]==id):
				stars=stars+(int(i["STARS"]))
				x=x+1
		print(i["BUSINESS_ID"])
		print(id)
		return (stars/x)





def main(id):
	a=avg()
	return(a.run((id)))

if __name__ == '__main__':
    main()

