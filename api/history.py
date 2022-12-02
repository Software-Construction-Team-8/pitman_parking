from flask import Flask,jsonify, render_template, request, redirect,Blueprint
from pymongo import MongoClient
from flask_cors import CORS

history = Blueprint('history', __name__)
CORS(history)

client = MongoClient('mongodb+srv://sc_delaEmi:u2JsEd0nzYssgaMd@cluster0.8qczawe.mongodb.net/test', 5000)
db=client['test']
History = db.History


@history.route("/history/print")
def print_history():
    #Database List
    arr = list(History.find({}, {"_id":1, "Identifier":1, "Space ID":1, "Space Occupied":1, "Level Number":1, "Space Number":1}))
    return render_template("./history.html", title="History", data=arr)