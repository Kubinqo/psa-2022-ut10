#!/user/bin/env python3
from flask import Flask, jsonify, request

AUTA = [
    {"id":0, "znacka": "Porsche", "model": "GT3 RS", "vykon": 386},
    {"id":1, "znacka": "Skoda", "model": "Felicia", "vykon": 50}
    ]

api = Flask(__name__)

@api.route("/")
def index():
    return "<h1>API index</h1></br>Flaskove API Autobazara"

#---------------------DajVsetko---------------------------------
@api.route("/auta")
def dajAuta():
    return jsonify(AUTA)

#----------------------Funkcia----------------------------------
def dajPrvokID(id):
    for auto in AUTA:
        if (auto.get("id") == id):  #
            return auto
    return None

#------------------------Daj-------------------------------------
@api.route("/auta/<int:id>")
def dajAuto(id):
    auto = dajPrvokID(id)

    if (auto == None):
        return jsonify({"Error": "Index nenajdeny!"}), 404
    else:
        return jsonify(auto)

#---------------------Vymaz-----------------------------        
@api.route("/auta/<int:id>", methods=["DELETE"])
def vymazAuto(id):
    auto = dajPrvokID(id)

    if (auto == None):
        return jsonify({"Error": "Index nenajdeny!"}), 404
    else:
        AUTA.remove(auto)
        return jsonify(auto), 202

#---------------------Vytvor--------------------------------
@api.route("/auta", methods=["POST"])
def vytvorAuto():
    auto = request.json

    lastID = 0
    for i in AUTA:
        if (i.get("id") > lastID):
            lastID = i.get("id")
    
    auto["id"] =  lastID + 1          #nastav id

    AUTA.append(auto)
    return jsonify(auto), 201

#---------------------UPRAV------------------------------
@api.route("/auta/<int:id>", methods=["PATCH"])
def upravAuto(id):
    parametre = request.json
    auto = dajPrvokID(id)

    if (auto == None):
        return jsonify({"Error": "Index nenajdeny!"}), 404

    if ("znacka" in parametre):
        auto["znacka"] = parametre["znacka"]
    
    if ("model" in parametre):
        auto["model"] = parametre["model"]
    
    if ("vykon" in parametre):
        auto["vykon"] = parametre["vykon"]

    lastID = 0
    for i in AUTA:
        if (i.get("id") > lastID):
            lastID = i.get("id")
    
    auto["id"] =  lastID + 1          #nastav id

    AUTA.append(auto)
    return jsonify(auto), 201

#------------------------------------------------------------
if __name__ == "__main__":
    api.run("0.0.0.0", 8888)