from flask import Flask,jsonify
app=Flask(__name__)
@app.route('/data')
def greet():
    a = {
        "name" : "Arathy",
        "age" : 16,
        "class": 10,
        "Address":"Sreerangam venganoor",
        "Roll_no" : 12,
        "Register_no":123456,
    }
    
    return jsonify(a)
app.run(debug=True)