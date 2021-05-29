import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
# need to import env package in order to use environment variables
# import env only if the os can find an existing file path for
# the env.py path itself (not pushed, Heroku won't be able to find it)
from flask_pymongo import PyMongo
# Needed to render object id. Mongodb stores its data in BSON format
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


# create instance of Flask in variable 'app'
app = Flask(__name__)

# app settings
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# create instance of PyMongo and pass the app into it
# to ensure app is communicating with DB
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


# tell app how and where to run application
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # set to false prior to submission
            debug=True)
