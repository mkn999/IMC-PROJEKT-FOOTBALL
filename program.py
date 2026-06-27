from flask import Flask
app=Flask(__name__)
@app.route('/signin')
def greet():
   return("Welcome to ")
app.run(debug=True)
 