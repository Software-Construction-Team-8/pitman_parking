from flask import Flask, render_template, redirect, Blueprint, url_for
from pymongo import MongoClient
from flask_cors import CORS

database = Blueprint('database', __name__)

CORS(database)

client = MongoClient('mongodb+srv://sc_delaEmi:u2JsEd0nzYssgaMd@cluster0.8qczawe.mongodb.net/test', 5000)
db=client['test']
garage = [db.Level_1, db.Level_2, db.Level_3, db.Level_4, db.Level_5]

#api calls (Methods)

@database.route("/database/printFloor")
def full_Database():
    arr = []
    for floor in garage:
        arr.append(list(floor.find({}, {"_id":1, "Space ID":1, "Space Occupied":2, "Level Number":3, "Space Number":4})))

    return render_template("./database.html", title="database", arr=arr )

@database.route("/garage/database/switchSpace/<id>", methods=["POST", "GET"])
def change_State(id):

    for floor in garage:
        arr = list(floor.find({}, {"_id":1, "Space ID":1, "Space Occupied":2, "Level Number":3, "Space Number":4}))
        lista = []
        for item in arr:
            lista.append(item["_id"])
            if str(lista[-1]) == str(id):
                arr.update_one({'_id': lista[-1]}, {"$set": {"Space Occupied": not item["Space Occupied"]}})
                break

    return redirect(url_for('database.full_Database'))

@database.route("/garage/database/clear", methods=["POST", "GET"])
def clear():
    for floor in garage:
        arr = list(floor.find({}, {"_id":1, "Space ID":1, "Space Occupied":2, "Level Number":3, "Space Number":4}))
        for item in arr:
            item.update_one({'_id': item["_id"]}, {"$set": {"Space Occupied": False}})
    return redirect(url_for('database.full_Database'))