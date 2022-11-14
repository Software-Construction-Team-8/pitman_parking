from flask import Flask,jsonify, render_template,request,redirect
from pymongo import MongoClient
from flask_cors import CORS




app = Flask(__name__)

CORS(app)

client = MongoClient('mongodb+srv://sc_delaEmi:u2JsEd0nzYssgaMd@cluster0.8qczawe.mongodb.net/test', 5000)
db=client['test']
project = db.Parking_Sopts

@app.route("/")
def home_page():
    return render_template("./home.html", title="Homepage")

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

@app.route("/getall")
def get_all_packets():
    things = []
    for thing in project.find():
        things.append(thing)
        print(thing)
    return str(things)


if __name__ == "__main__":
    app.run(debug=True)

