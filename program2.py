from flask import Flask,jsonify
app=Flask(__name__)
@app.route('/')
def greet():
    a={"Name":"Swathi","Age":"12","Class":"10","Roll no":"12","Address":"Swathi Nivas,Manvila","Reg.no":"25017115"}
    return jsonify(a)
app.run(debug=True)
