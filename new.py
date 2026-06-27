from flask import Flask,jsonify
app = Flask(__name__)
app.route('/')
def greet():
    a={
        'name':'arathy'
    }
    return jsonify(a)
app.run(debug=True)
