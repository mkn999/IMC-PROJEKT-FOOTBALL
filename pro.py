from flask import Flask

app = Flask(__name__)
@app.route('/login')
def login():
    return "hello user"
app.run(debug=True)

