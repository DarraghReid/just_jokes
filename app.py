import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
# Needed to render object id. Mongodb stores its data in BSON format
from bson.objectid import ObjectId
# import password security features for registration page
from werkzeug.security import generate_password_hash, check_password_hash
# need to import env package in order to use environment variables
# import env only if the os can find an existing file path for
# the env.py path itself (not pushed, Heroku won't be able to find it)
if os.path.exists("env.py"):
    import env


# create instance of Flask in variable 'app'
app = Flask(__name__)

# app settings
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# create instance of PyMongo and pass the app into it
# to ensure app is communicating with database
mongo = PyMongo(app)


# decorator with route to get_jokes() function
# it will redirect to/call this function when attached to a url
# this function renders jokes.html?
@app.route("/")
@app.route("/get_jokes")
def get_jokes():
    # find all docs from jokes collection in MongoDB
    jokes = mongo.db.jokes.find()
    # render jokes.html template, pass jokes variable into it
    return render_template("jokes.html", jokes=jokes)


# GET is default
@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        # check if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # inform user if username has been taken
        if existing_user:
            flash("username already exists")
            return redirect(url_for("sign_up.html"))

        # compile dictionary of user's data
        sign_up = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "date_of_birth": request.form.get("date")
        }

        # insert user into database
        mongo.db.users.insert_one(sign_up)

        # put new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("You're signed up!")

    return render_template("sign_up.html")


# tell app how and where to run application
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # set to false prior to submission
            debug=True)
