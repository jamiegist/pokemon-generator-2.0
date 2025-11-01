from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_pokemon():
    url = ""
    responose = json.loads(requests.request("GET", url).text)
    pokemon_large = response["preview"][-2]
    pokemon_name = response["pokemon"]
    return pokemon_large, pokemon

@app.route("/")
def index():
    pokemon_pic,pokemon_name = get_pokemon()
    return render_template("index.html", pokemon_pic=pokemon_pic, pokemon_name=pokemon_name)

# app.run(host="0.0.0.0", port=80) #