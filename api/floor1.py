from flask import Flask, render_template, redirect, Blueprint, url_for
from pymongo import MongoClient
from flask_cors import CORS

floor1 = Blueprint('floor1', __name__)
CORS(floor1)

client = MongoClient('mongodb+srv://sc_delaEmi:u2JsEd0nzYssgaMd@cluster0.8qczawe.mongodb.net/test', 5000)
db=client['test']
project = db.Level_1
history = db.History

#api calls (Methods)

@floor1.route("/garage/floor1/printFloor")
def garage_level1():
    #Database List
    left, right, center = [],[],[]
    arr = list(project.find({}, {"_id":1, "Space ID":1, "Space Occupied":1, "Level Number":1, "Space Number":1}))

    for i in arr:
        if i["Space Number"] % 3 == 0:
            print(i["Space Number"] % 3)
            right.append(i)

        if i["Space ID"] % 3 == 1:
            left.append(i)

        if i["Space ID"] % 3 == 2:
            center.append(i)

    return render_template("./garage.html", title="Floor1", left=left, right=right, center=center )

@floor1.route("/garage/floor1/switchSpace/<id>", methods=["POST", "GET"])
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

    return redirect(url_for('floor1.garage_level1'))

@floor1.route("/garage/floor1/clear", methods=["POST", "GET"])
def update_space():
    arr = list(project.find({}, {"_id":1, "Space ID":1, "Space Occupied":2, "Level Number":3, "Space Number":4}))
    for item in arr:
        project.update_one({'_id': item["_id"]}, {"$set": {"Space Occupied": False}})
    return redirect(url_for('floor1.garage_level1'))

    