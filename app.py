import os
import datetime
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


@app.route("/")
@app.route("/get_jokes")
def get_jokes():

    # find user's date of birth from the database
    db_dob = mongo.db.users.find_one(
        {"username": session["user"]})["date_of_birth"]

    # get user's year of birth from db_dob
    user_y = int(db_dob[0:4])

    # get user's month of birth from db_dob
    user_m = int(db_dob[5:7])

    # get user's day of birth from db_dob
    user_d = int(db_dob[8:])

    # make datetime object out of dob info
    dob = datetime.date(user_y, user_m, user_d)

    # calculate user's dob
    def calculate_age(born):
        # today's date
        today = datetime.datetime.today()
        return today.year - born.year - (
            (today.month, today.day) < (born.month, born.day))

    user_age = calculate_age(dob)

    # find all jokes from jokes collection in MongoDB
    jokes = list(mongo.db.jokes.find())

    # find all age appropriate jokes from jokes collection in MongoDB
    age_app_jokes = list(mongo.db.jokes.find({"for_children": "on"}))

    # find all favourites from user_favourites collection in MongoDB
    fav_jokes = list(mongo.db.user_favourites.find())

    # render jokes.html template, pass jokes variable into it
    return render_template(
        "jokes.html", jokes=jokes, fav_jokes=fav_jokes, user_age=user_age,
        age_app_jokes=age_app_jokes)


@app.route("/search", methods=["GET", "POST"])
def search():
    search = request.form.get("search")

    # find all docs from jokes collection in MongoDB
    jokes = list(mongo.db.jokes.find({"$text": {"$search": search}}))

    # render jokes.html template, pass jokes variable into it
    return render_template("jokes.html", jokes=jokes)


# GET is default
@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        # check database for input username
        user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # inform user if username has been taken
        if user:
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
        return redirect(url_for(
            "profile", username=session["user"]))

    return render_template("sign_up.html")


@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        # check mongodb for input username
        user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # if username exists, check if input password matches hashed password
        if user:
            if check_password_hash(
                user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    # if passwords match, put user into session
                    flash("Welcome, {}!".format(request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            # if passwords don't match, inform user and have them try again
            else:
                flash("Incorrect username and/or password")
                return redirect(url_for("sign_in"))

        # if username doesn't exist, inform user and have them try again
        else:
            flash("Incorrect username and/or password")
            return redirect(url_for("sign_in"))

    return render_template("sign_in.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # set username variable equal to username of session user
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    # find all docs from jokes collection in MongoDB
    jokes = list(mongo.db.jokes.find())

    # find all favourites from user_favourites collection in MongoDB
    fav_jokes = list(mongo.db.user_favourites.find())

    # render template with above variables only if session user is truthy
    if session["user"]:
        return render_template(
            "profile.html",
            username=username, jokes=jokes, fav_jokes=fav_jokes)

    return redirect(url_for("sign_in"))


@app.route("/add_fav/<joke_id>", methods=["GET", "POST"])
def add_fav(joke_id):
    # search users for joke passed into view
    joke = mongo.db.jokes.find_one({"_id": ObjectId(joke_id)})

    # compile dictionary of joke details
    fav_joke = {
        "joke_title": joke["joke_title"],
        "joke_description": joke["joke_description"],
        "img_url": joke["img_url"],
        "for_children": joke["for_children"],
        "joke_teller": joke["joke_teller"],
        "favouriter": session["user"]
     }

    # search user_favourites for indentical joke
    already_favd = mongo.db.user_favourites.find_one(
        {"joke_description": joke["joke_description"]})

    # if jokes match, inform user they have already favourited this joke
    if joke["joke_description"] == already_favd["joke_description"]:
        flash("Joke already favourited")
        return redirect(url_for("get_jokes"))
    # otherwise, insert fav_joke into dictionary
    else:
        mongo.db.user_favourites.insert_one(fav_joke)
        flash("Joke favourited!")
        return redirect(url_for("get_jokes"))

    return render_template("jokes.html")


@app.route("/remove_fav/<joke_id>")
def remove_fav(joke_id):
    mongo.db.user_favourites.remove({"_id": ObjectId(joke_id)})
    flash("Removed from favourites")
    return redirect(url_for(
            "profile", username=session["user"]))


@app.route("/sign_out")
def sign_out():
    # remove user from session cookies
    flash("Signed out")
    session.pop("user")
    return redirect(url_for("sign_in"))


@app.route("/add_joke", methods=["GET", "POST"])
def add_joke():
    if request.method == "POST":
        # set for_children to "on" in db if for_children switch is truthy
        for_children = "on" if request.form.get("for_children") else "off"
        # compile dictionary of joke details
        joke = {
            "joke_title": request.form.get("joke_title"),
            "joke_description": request.form.get("joke_description"),
            "img_url": request.form.get("img_url"),
            "for_children": for_children,
            "joke_teller": session["user"]
        }
        # insert dictionary into db
        mongo.db.jokes.insert_one(joke)
        flash("Joke Added!")
        return redirect(url_for("add_joke"))

    return render_template("add_joke.html")


@app.route("/edit_joke/<joke_id>", methods=["GET", "POST"])
def edit_joke(joke_id):
    if request.method == "POST":
        # set for_children to "on" in db if for_children switch is truthy
        for_children = "on" if request.form.get("for_children") else "off"
        # compile dictionary of joke details
        edited_joke = {
            "joke_title": request.form.get("joke_title"),
            "joke_description": request.form.get("joke_description"),
            "img_url": request.form.get("img_url"),
            "for_children": for_children,
            "joke_teller": session["user"]
        }
        # insert dictionary into db
        mongo.db.jokes.update({"_id": ObjectId(joke_id)}, edited_joke)
        flash("Joke Edited!")
        return redirect(url_for("get_jokes"))
        # return redirect(url_for("add_joke(your_jokes"))

    # find joke by id key in db, convert id to bson format
    joke = mongo.db.jokes.find_one({"_id": ObjectId(joke_id)})

    return render_template("edit_joke.html", joke=joke)


@app.route("/delete_joke/<joke_id>")
def delete_joke(joke_id):
    mongo.db.jokes.remove({"_id": ObjectId(joke_id)})
    flash("Joke removed")
    return redirect(url_for("get_jokes"))


# tell app how and where to run application
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # set to false prior to submission
            debug=True)
