import time
#from flask import Flask
from flask import Flask,jsonify, render_template,request,redirect
#from flask_pymongo import PyMongo
from pymongo import MongoClient




app = Flask(__name__)

client = MongoClient('mongodb+srv://sc_delaEmi:u2JsEd0nzYssgaMd@cluster0.8qczawe.mongodb.net/test', 5000)
db=client['test']
project = db.Sample

@app.route('/hello')
def hello():
    return 'Hello world'


@app.route('/mongotest', methods=["POST", "GET"])
def mongotest():
    id = "prk"
    data = "dta"
    packet = {"id": id, "data": data}
    post_id = project.insert_one(packet).inserted_id
    return "Added to db"

