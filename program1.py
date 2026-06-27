from flask import Flask,jsonify
app=Flask(__name__)
@app.route('/login')
def greet():
    a={"name":"Swathi", "age":"18","School":"St.Mary's"}
    return jsonify(a) 
app.run(debug=True)