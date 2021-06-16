import os
# to calculate user's age
import datetime
# for app functionality
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
# for pagination
from flask_paginate import Pagination, get_page_args
# to work with MongoDB
from flask_pymongo import PyMongo
# to render object id. Mongodb stores its data in BSON format
from bson.objectid import ObjectId
# import password security features for registration page
from werkzeug.security import generate_password_hash, check_password_hash
# need to import env package in order to use environment variables
# import env only if the os can find an existing file path for
# the env.py path itself (not pushed, Heroku won't be able to find it)
if os.path.exists("env.py"):
    import env

# Pagination activity limit
PER_PAGE = 8

# create instance of Flask in variable 'app'
app = Flask(__name__)

# app settings
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# create instance of PyMongo and pass the app into it
# to ensure app is communicating with database
mongo = PyMongo(app)


# Pagination
# https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
def paginated(jokes):
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    offset = page * PER_PAGE - PER_PAGE

    return jokes[offset: offset + PER_PAGE]


def pagination_args(jokes):
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page')
    total = len(jokes)

    return Pagination(page=page, per_page=PER_PAGE, total=total)


# calculates user's age
def get_age():
    if "user" in session:
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
        return user_age


# gets all jokes, age appropriate jokes, renders jokes.html
@app.route("/")
@app.route("/get_jokes")
def get_jokes():

    # get user's age from get_age()
    user_age = get_age()

    # find all favourites from user_favourites collection in MongoDB
    fav_jokes = list(mongo.db.user_favourites.find())

    if int(user_age) >= 18:
        # find all jokes from jokes collection in MongoDB
        jokes = list(mongo.db.jokes.find())

        # pagination of jokes
        jokes_paginated = paginated(jokes)
        pagination = pagination_args(jokes)

        # render jokes.html template, pass variables into it
        return render_template(
            "jokes.html",
            jokes=jokes_paginated,
            fav_jokes=fav_jokes,
            user_age=user_age,
            pagination=pagination,
            )
    else:
        # find all age appropriate jokes from jokes collection in MongoDB
        age_app_jokes = list(mongo.db.jokes.find({"for_children": "on"}))

        # pagination of age appropriate jokes
        age_app_jokes_paginated = paginated(age_app_jokes)
        pagination = pagination_args(age_app_jokes)

        # render jokes.html template, pass variables into it
        return render_template(
            "jokes.html",
            fav_jokes=fav_jokes,
            user_age=user_age,
            age_app_jokes=age_app_jokes_paginated,
            pagination=pagination,
            )


# takes search word from search input, display list of jokes with that word
@app.route("/search", methods=["GET", "POST"])
# take user_age from get_jokes() view
def search():
    search = request.form.get("search")

    # get user's age from get_age()
    user_age = get_age()

    # find all age appropriate jokes from jokes collection in MongoDB
    # age_app_jokes = list(mongo.db.jokes.find({"for_children": "on"}))

    # find all docs from jokes collection in MongoDB
    jokes = list(mongo.db.jokes.find({"$text": {"$search": search}}))

    # render jokes.html template, pass jokes variable into it
    return render_template(
        "jokes.html",
        jokes=jokes,
        user_age=user_age
        )


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        # check database for input username
        user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # inform user if username has been taken
        if user:
            flash("username already exists")
            return redirect(url_for("sign_up"))

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

    fav_jokes = []

    # find all docs from jokes collection in MongoDB
    jokes = list(mongo.db.jokes.find())

    # find all jokes that user has favourited
    for joke in jokes:
        favourites = joke["favouriter"]
        for name in favourites:
            if name == session["user"]:
                fav_jokes.append(joke)

    # pagination of favourite jokes
    fav_jokes_paginated = paginated(fav_jokes)
    pagination = pagination_args(fav_jokes)

    # render template with above variables only if session user is truthy
    if session["user"]:
        return render_template(
            "profile.html",
            username=username,
            jokes=jokes,
            fav_jokes=fav_jokes_paginated,
            pagination=pagination
            )

    return redirect(url_for("sign_in"))


@app.route("/add_fav/<joke_id>", methods=["GET", "POST"])
def add_fav(joke_id):
    # search users for joke passed into view
    joke = mongo.db.jokes.find_one({"_id": ObjectId(joke_id)})

    # get the array of users who favourited the joke
    favouriter_array = joke["favouriter"]

    # loop through array to check if user has already liked the joke
    for name in favouriter_array:
        # if user's name is in the array,
        # not_favourited is False, otherwise it's True
        # use negative values to avoid duplication
        if name == session["user"]:
            not_favourited = False
        elif name != session["user"]:
            not_favourited = True

    # if the user hasn't favourited the joke, add user's
    # name to array of users who favourited the joke
    if not_favourited:
        # insert user's name into the favouriter_array array
        favouriter_array.append(session['user'])

        # update db with dictionary
        mongo.db.jokes.update_one(
            {"_id": ObjectId(joke_id)},
            {"$set": {"favouriter": favouriter_array}})

        flash("Joke favourited!")
        return redirect(url_for("get_jokes"))

    # if user has favourited the joke
    else:
        # inform user they have already favou this joke.
        flash("Joke already favourited")
        return redirect(url_for("get_jokes"))

    return render_template("jokes.html")


@app.route("/like_joke/<joke_id>", methods=["GET", "POST"])
def like_joke(joke_id):
    # search users for joke passed into view
    joke = mongo.db.jokes.find_one({"_id": ObjectId(joke_id)})

    # determine how many like the joke currently has
    prev_likes = joke["likes"]

    # increment joke's likes by 1
    new_likes = int(prev_likes) + 1

    # get the array of users who like the joke
    liked_by_array = joke["liked_by"]

    # loop through array to check if user has already liked the joke
    for name in liked_by_array:
        # if user's name is in the array,
        # not_liked is False, otherwise it's True
        # use negative values to avoid duplication
        if name == session["user"]:
            not_liked = False
        elif name != session["user"]:
            not_liked = True


    # if the user hasn't liked the joke, add user's
    # name to array of users who liked the joke
    if not_liked:
        # insert user's name into the liked_by array
        liked_by_array.append(session['user'])

        # update array in db
        mongo.db.jokes.update_one(
            {"_id": ObjectId(joke_id)},
            {"$set": {"liked_by": liked_by_array}})

        # update "likes" in db
        mongo.db.jokes.update_one(
            {"_id": ObjectId(joke_id)},
            {"$set": {"likes": new_likes}})

        flash("You've liked this joke!")
        return redirect(url_for("get_jokes"))

    # if user hasn't liked the joke
    else:
        # inform user they have already liked this joke.
        flash("You've already liked this joke")
        return redirect(url_for("get_jokes"))

    return render_template("jokes.html")


@app.route("/remove_fav/<joke_id>")
def remove_fav(joke_id):
    mongo.db.user_favourites.remove({"_id": ObjectId(joke_id)})
    flash("Removed from favourites")
    return redirect(url_for(
            "profile", username=session["user"]))


@app.route("/unlike_joke/<joke_id>")
def unlike_joke(joke_id):
    # search users for joke passed into view
    joke = mongo.db.jokes.find_one({"_id": ObjectId(joke_id)})

    prev_likes = joke["likes"]
    new_likes = prev_likes - 1

    # compile dictionary of joke details
    liked_joke = {
        "joke_title": joke["joke_title"],
        "joke_description": joke["joke_description"],
        "img_url": joke["img_url"],
        "for_children": joke["for_children"],
        "joke_teller": joke["joke_teller"],
        "likes": new_likes
    }

    # insert dictionary into db
    mongo.db.jokes.update({"_id": ObjectId(joke_id)}, liked_joke)
    flash("You've unliked this joke")
    return redirect(url_for("get_jokes"))


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
            "joke_teller": session["user"],
            "likes": 0,
            "liked_by": ["name"],
            "favouriter": ["name"]
        }
        # insert dictionary into db
        mongo.db.jokes.insert_one(joke)
        flash("Joke Added!")
        return redirect(url_for("add_joke"))

    return render_template("add_joke.html")


@app.route("/edit_joke/<joke_id>", methods=["GET", "POST"])
def edit_joke(joke_id):

    # find joke by id key in db
    joke = mongo.db.jokes.find_one({"_id": ObjectId(joke_id)})

    if request.method == "POST":
        # set for_children to "on" in db if for_children switch is truthy
        for_children = "on" if request.form.get("for_children") else "off"

        # compile dictionary of joke details
        edited_joke = {
            "joke_title": request.form.get("joke_title"),
            "joke_description": request.form.get("joke_description"),
            "img_url": request.form.get("img_url"),
            "for_children": for_children,
            "joke_teller": session["user"],
            "likes": joke["likes"],
            "liked_by": joke["liked_by"],
            "favouriter": joke["favouriter"]
        }
        # insert dictionary into db
        mongo.db.jokes.update({"_id": ObjectId(joke_id)}, edited_joke)
        flash("Joke Edited!")
        return redirect(url_for("get_jokes"))
        # return redirect(url_for("profile(your_jokes"))

    return render_template(
        "edit_joke.html",
        joke=joke
        )


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
