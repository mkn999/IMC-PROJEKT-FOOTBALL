from flask import Flask,jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data = {
    "match1":{
    "venue":"Houstoun",
    "time":"12:30 am",
    "awayTeam":"Argentina",
    "homeTeam":"Brazil",
    "homeTeamFlag":"https://upload.wikimedia.org/wikipedia/en/0/05/Flag_of_Brazil.svg",
    "awayTeamFlag":"https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Flag_of_Argentina.svg/960px-Flag_of_Argentina.svg.png"
    },
    "match2":{
    "venue":"Houstoun",
    "time":"12:30 am",
    "awayTeam":"France",
    "homeTeam":"Spain",
    "homeTeamFlag":"https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Flag_of_Spain.svg/1280px-Flag_of_Spain.svg.png",
    "awayTeamFlag":"https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Flag_of_France_%281790%E2%80%931794%29.svg/250px-Flag_of_France_%281790%E2%80%931794%29.svg.png"
    },

}

@app.route("/test")
def greet():
    headers = {
        "x-auth-token":"28242fce050d42118b6e9b9863124f97",
    }

    response = requests.get("https://api.football-data.org/v4/matches",
                            headers=headers)
    teams = []
    data = response.json()
    realdata = data["matches"]
    for match in realdata:
        teams.append(match["awayTeam"]["name"] + " vs " + match["homeTeam"]["name"])
    return "<br>".join(teams)



@app.route("/matches")
def matches():
    return jsonify(data)

app.run(debug=True)