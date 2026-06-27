from flask import Flask,jsonify
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
@app.route('/data')
def greet():
    a = {
        "name" : "Arathy",
        "age" : 16,
        "class": 10,
        "address":"Sreerangam venganoor",
        "rnumber" : 12,
        "registerNumber":123456,
    }

    return jsonify(a)
app.run(debug=True)