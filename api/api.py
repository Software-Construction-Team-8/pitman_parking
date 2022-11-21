from flask import Flask, jsonify, render_template, request, redirect, Blueprint
from pymongo import MongoClient
from flask_cors import CORS

#Blueprints
from floor1 import floor1
from floor2 import floor2
from floor3 import floor3
from floor4 import floor4
from floor5 import floor5

app = Flask(__name__)
app.register_blueprint(floor1)
app.register_blueprint(floor2)
app.register_blueprint(floor3)
app.register_blueprint(floor4)
app.register_blueprint(floor5)

CORS(app)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("./home.html", title="Homepage")

@app.route("/garage")
def garage_page():
    #Database List
    arr = list(project.find({}, {"_id":1, "Space ID":1, "Space Occupied":2, "Level Number":3, "Space Number":4}))
    return render_template("./garage.html", title="Garage", data=arr)

@app.route("/street")
def street_page():
    return render_template("./garage.html", title="Garage")


@app.route('/hello')
def hello():
    return 'Hello world'


@app.route('/mongotest', methods=["POST", "GET"])
def mongotest():
    id = "prk"
    data = "dta"
    lev_num = "x"
    sp_num = "x"
    packet = {"Space ID": id, "Space Occupied": data, "Level Number": lev_num, "Space Number": sp_num}
    post_id = project.insert_one(packet).inserted_id
    return "Added to db"

#@app.route("/getall")
#def get_all_packets():

    
