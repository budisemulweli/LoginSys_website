
from flask import Flask, redirect, render_template, request
from replit import db

# imports request and redirect as well as flask

app = Flask(__name__, static_url_path='/static')
# path to the static file that stores my images

# db["david"] = {"password" : "Baldy1"}
# db["katie"] = {"password" : "k8t"}
# A dictionary hard coded into the program that stores the login details for two users


@app.route('/Create')
def create():
  return render_template('create.html')

@app.route('/process', methods=["POST", "GET"])
def save_user():
    keys = list(db.keys())
    form = request.form
    if request.method == "POST":
      if form["username"] not in keys:
        name = form["name"]
        username = form["username"]
        password = form["password"]
        db[username] = {"name": name,"password":password}
        
      else:
        return '''
               <p>User already exists</p>
               <br>
               <a href="/login">Login instead</a>
               <a href="/Create">Sign up another user</a>'''
    return redirect('/login')


@app.route('/login', methods=["POST", "GET"])
def login():
    form = request.form
    keys = list(db.keys())
    if request.method == "POST":
      print(f"{db[form['username']]['password']} and {db[form['username']]}")
      try:
          if form["username"] in keys and  db[form["username"]]["password"] == form["password"]: 
            return f"Hello, {db[form['username']]['name']}"
          else:
            return '''
             <p>User credentials invalid</p>
             <br>
             <a href="/login">Login again</a>
             <a href="/Create">Sign up</a>'''
      except:
        return '''
         <p>Error Occured</p>
         <br>
         <a href="/login">Login</a>
         <a href="/Create">Sign up</a>'''
        
    return render_template("login.html")



# @app.route('/changePass', methods = ["POST"])
# def changepass():
#   formpass = request.form["newPassword"]
#   username = request.form["username"]
#   db[username]["password"] = formpass
#   print(f"password changed to {formpass}")
#   return redirect("/")


@app.route('/')
def index():
  return '''
    <a href="/Create">Sign Up</a>
    <br>
    <br>
    <a href="/login">Login</a>
  '''


app.run(host='0.0.0.0', port=81)
