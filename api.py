
#Import the libraries 
from flask import Flask
from flask import request
from bson.json_util import dumps
from bson.objectid import ObjectId
from pymongo import MongoClient
client = MongoClient()
celebrities = client.cinema.celebrities
movies = client.cinema.movies

# Función que saca la info de la collection celebrities a través del objectid.
def info(id):
    filt = {"_id":ObjectId(id)}
    proyect = {"_id":0}
    result = celebrities.find(filt,proyect)
    return list(result)

def insert_celebritie(name,occupation,catch_phrase):
    
    dic = {"name":f"{name}",
      "occupation":f"{occupation}",
      "catch_phrase":f"{catch_phrase}"}
    
    return celebrities.insert_one(dic)


app = Flask(__name__)

#Endpoints funciones con decoradores.
@app.route("/")
def root():
    saludo = {"Hola bienvenido" :"estas entrando en la api de Ana"}
    return dumps(saludo)

@app.route("/celebrities")
def find_all_celebrities(celebrities):
    filt = {}
    proyect = {"_id":1,"name":1}
    result = celebrities.find(filt,proyect)
    return dumps(list(result))

@app.route("/celebrities/details/<id>")
def find_details_celebrities(id):
    id = str(id)
    try:
        info_id = info(id)
        return dumps(info_id)
    except:
        return "Error de Id, vuelve a intentarlo"

@app.route("/celebrities/new/<name>/<occupation>/<catch_phrase>")
def insert_celebrities(name,occupation,catch_phrase):

 # Revisar el if porque no me lo está cogiendo bien.
    if celebrities["name"] == "name":
        return "Ya existe en nuestra base de datos. Prube con otro"
    else: 
        insert_celebritie(name,occupation,catch_phrase)
        return "ok."




app.debug=True
app.run()