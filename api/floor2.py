from flask import Flask, render_template, redirect, Blueprint, url_for
from pymongo import MongoClient
from flask_cors import CORS

floor2 = Blueprint('floor2', __name__)

CORS(floor2)

client = MongoClient('mongodb+srv://sc_delaEmi:u2JsEd0nzYssgaMd@cluster0.8qczawe.mongodb.net/test', 5000)
db=client['test']
project = db.Level_2
history = db.History
#api calls (Methods)

@floor2.route("/garage/floor2/printFloor")
def garage_level2():
    #Database List
    left, right, center = [],[],[]
    arr = list(project.find({}, {"_id":1, "Space ID":1, "Space Occupied":2, "Level Number":3, "Space Number":4}))

    for i in arr:
        if i["Space Number"] % 3 == 0:
            print(i["Space Number"] % 3)
            right.append(i)

        if i["Space ID"] % 3 == 1:
            left.append(i)

        if i["Space ID"] % 3 == 2:
            center.append(i)

    return render_template("./big_garage.html", title="floor2", left=left, right=right, center=center )

@floor2.route("/garage/floor2/switchSpace/<id>", methods=["POST", "GET"])
def switch_space(id):
    arr = list(project.find({}, {"_id":1, "Space ID":1, "Space Occupied":2, "Level Number":3, "Space Number":4}))

    lista = []

    for item in arr:
        lista.append(item["_id"])
        if str(lista[-1]) == str(id):
            hist = {"Identifier": item["_id"], "Space ID":item["Space ID"], "Space Occupied":item["Space Occupied"], "Level Number":item["Level Number"], "Space Number":item["Space Number"]}
            history.insert_one(hist).inserted_id
            project.update_one({'_id': lista[-1]}, {"$set": {"Space Occupied": not item["Space Occupied"]}})
            break
    return redirect(url_for('floor2.garage_level2'))

@floor2.route("/garage/floor2/clear", methods=["POST", "GET"])
def update_space():
    arr = list(project.find({}, {"_id":1, "Space ID":1, "Space Occupied":2, "Level Number":3, "Space Number":4}))
    for item in arr:
        project.update_one({'_id': item["_id"]}, {"$set": {"Space Occupied": False}})
    return redirect(url_for('floor2.garage_level2'))

    