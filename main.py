from flask import Flask, render_template, jsonify, request
from API.module1 import calc_decimal
from API.module2 import convert_to_binary
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    if request.method == "GET":
        return render_template("index.html")

@app.route("/find_decimal", methods=["GET", "POST"])
def home2():
    if request.method == "GET":
        return render_template("binary_to_decimal.html")
    
    elif request.method == "POST":
        data = request.get_json()
        binary = data.get("binary")
        return calc_decimal(binary)
    
    else:
        return jsonify({"message": "Action not allowed"}), 401
    
@app.route("/find_binary", methods=["GET", "POST"])
def home3():
    if request.method == "GET":
        return render_template("binary_to_decimal.py")
    
    elif request.method == "POST":
        data = request.get_json()
        binary = data.get("decimal")
        return convert_to_binary(decimal)
    
    else:
        return jsonify({"message": "method not allowed" }), 401
    

















app.run()