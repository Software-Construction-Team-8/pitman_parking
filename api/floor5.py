from flask import Flask,jsonify, render_template, request, redirect,Blueprint
from pymongo import MongoClient
from flask_cors import CORS

floor5 = Blueprint('floor5', __name__)

CORS(floor5)

client = MongoClient('mongodb+srv://sc_delaEmi:u2JsEd0nzYssgaMd@cluster0.8qczawe.mongodb.net/test', 5000)
db=client['test']
project = db.Level_5
history = db.History
#api calls (Methods)

#Get all the spots on the Level 5
@floor5.route("/garage/floor5/printFloor")
def garage_level5():
    #Database List
    arr = list(project.find({}, {"_id":1, "Space ID":1, "Space Occupied":2, "Level Number":3, "Space Number":4}))
    return render_template("./garage.html", title="floor5", data=arr)


#Updates the state of a specific spot
@floor5.route("/garage/floor5/switchSpace/<id>", methods=["POST", "GET"])
def switch_space(id):
    arr = list(project.find({}, {"_id":1, "Space ID":1, "Space Occupied":2, "Level Number":3, "Space Number":4}))

    lista = []

    for item in arr:
        lista.append(item["_id"])
        if str(lista[-1]) == str(id):
            hist = {"Identifier": item["_id"], "Space ID":item["Space ID"], "Space Occupied":item["Space Occupied"], "Level Number":item["Level Number"], "Space Number":item["Space Number"]}
            history.insert_one(hist).inserted_id
            project.update_one({'_id': lista[-1]}, {"$set": {"Space Occupied": not item["Space Occupied"]}})
            return "Item Updated"
    return "Item not Found"

@floor5.route("/garage/floor5/clear", methods=["POST", "GET"])
def update_space():
    arr = list(project.find({}, {"_id":1, "Space ID":1, "Space Occupied":2, "Level Number":3, "Space Number":4}))
    for item in arr:
        project.update_one({'_id': item["_id"]}, {"$set": {"Space Occupied": True}})
    return "hi"