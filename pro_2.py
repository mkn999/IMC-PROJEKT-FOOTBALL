from flask import Flask,jsonify 

app = Flask(__name__)
@app.route('/')
def ser():
    user_profile = {"user_name":"reya rajesh","age": 17,"class":"12 B","admin_no":4162}
    return jsonify(user_profile)
app.run(debug=True)

