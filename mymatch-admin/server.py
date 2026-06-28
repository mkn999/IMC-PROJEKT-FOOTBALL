from flask import Flask,request,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# eTeams = ["Algeria","Belgium","Croatia","Denmark","England","France","Germany"]

enrolledTeams = {
    0:{
        "name":"Algeria",
        "image":"https://crests.football-data.org/algeria.svg",
    },
     1:{
        "name":"Argentina",
        "image":"https://crests.football-data.org/762.png",
    },
       2:{
        "name":"South Korea",
        "image":"https://crests.football-data.org/772.png",
    }
}


# enrolledTeams.update({
#     3:{
#         "name":"Croatia",
#         "image":"https://crests.football-data.org/699.svg",
#     }
# })


@app.route('/addteams', methods=["POST"])
def addTeams():
    data = request.get_json()
    newKey = len(enrolledTeams)
    enrolledTeams[newKey] = data
    # enrolledTeams.update({3:data})
    # print(enrolledTeams)
    return jsonify({
        "message":"data received sucessfully !"
    })
@app.route('/getteams')
def getTeams():
    return jsonify(enrolledTeams)


app.run(debug=True)
