from flask import Flask
from flask import request
from flask import render_template

import json
from pymongo import MongoClient
from settings import Settings
NEW_COLLECTION = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.NEW_USER] # collection name is nu  

USER_PROFILE = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.USER_PROFILE] # collection name is u  
from predict import main as mn
#import stringComparison
from new_user_recommender import new_user_query as new_user_query

from CALCULATE_COSINE import calc_cos
app = Flask(__name__)
app.config['DEBUG']=True



@app.route('/')
def my_form():

    x= render_template("home_page.html") # this should be the name of your html file
    return x

@app.route('/new_user/')
def new_user():
    x= render_template("new_user.html") # this should be the name of your html file
    return x

@app.route('/new_user/', methods=['POST'])
def new_user_data():
    text1 = request.form['text1']
    text2 = request.form['text2']
    text3 = request.form['text3']
    text4 = request.form['text4']
    text5 = request.form['text5']
    cal_cos_on=str(text4)+str(text5)
    print(cal_cos_on)



    if(text2!=""):
        NEW_COLLECTION.insert_one({
            "EMAIL":str(text1),
            "AGE":str(text2),
            "GENDER":str(text3),
            "CUSINE":str(text4),
            "ATTRIBUTES":str(text5)

            })
        
        USER_PROFILE.insert_one({
                "USER_ID": str(text1),
                "ENCRYPTED":str(mn(cal_cos_on))})

    data = new_user_query(str(text4),text1)
    return render_template('new_user_display.html',**data)

@app.route('/existing_user/')
def existing_user():

    x= render_template("existing_user.html") # this should be the name of your html file
    return x

@app.route('/existing_user/', methods=['POST'])
def existing_user_data():
    text6 = request.form['text6']
    print("calc_cos:\n",text6)
    data = calc_cos(str(text6))
    return render_template('display.html',**data)


    

if __name__ == '__main__':
    app.run()