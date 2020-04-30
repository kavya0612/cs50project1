from flask import Flask, render_template, request, session
from flask_session import Session
from models import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (("postgresql://postgres:****@localhost:5432/project1"))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db.init_app(app)

users = []
@app.route("/", methods=["GET", "POST"])
@app.route("/index")
def index():
    if session.get("users") == 1:
        session["users"] = [1]
    if request.method == "POST":
        user = request.form.get("users")
        
    return render_template("index.html", user=users)

@app.route("/save", methods=["GET" , "POST"])
def save():
    name = request.form.get("name")
    password = request.form.get("password")

    check = User.query.filter_by(user_name=name).first()
    if check != None:
        return render_template("error.html", message="User name already exists.")

    user = User(user_name=name, password=password)
    db.session.add(user)
    db.session.commit()

    return render_template("success.html", message="Successfully registered")

@app.route("/register", methods=["GET" , "POST"])
def register():
    return render_template("register.html")

