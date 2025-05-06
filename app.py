# app.py
from flask import Flask, request, jsonify, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("SPOONACULAR_API_KEY")      #{Attention!!!  Use your own API key in .env file. I have used spoonacular API for this project.}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_recipe():
    data = request.get_json()
    ingredients = data.get("ingredients")

    if not ingredients:
        return jsonify({"error": "No ingredients provided"}), 400

    url = f"https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        "ingredients": ingredients,
        "number": 5,
        "apiKey": API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        recipes = response.json()
        return jsonify({"recipes": recipes})
    else:
        return jsonify({"error": response.text}), response.status_code

if __name__ == "__main__":
    app.run(debug=True)
