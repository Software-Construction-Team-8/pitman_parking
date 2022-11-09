import time
from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient

client = MongoClient('mongodb+srv://sc_delaEmi:u2JsEd0nzYssgaMd@cluster0.8qczawe.mongodb.net/test', 5000)
db = client['Software_Constrution']
project = db.Sample

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello world'
