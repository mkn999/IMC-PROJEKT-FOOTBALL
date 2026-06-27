from flask import Flask,jsonify
app = Flask(__name__)
@app.route('/')
def ser():
    student_profile = {"student_name":"reya","age":17,"class":"12 B","roll_no":31,"reg_no":4162,"address":"veli"}
    return jsonify(student_profile)
app.run(debug=True)
