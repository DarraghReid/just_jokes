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

# jokes per page
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

from pymongo import TEXT # import TEXT to create text index for search functionality. Needed for search functionality because MongoDB does not support full-text search by default. so this allows us to create a text index on specific fields in the collection, enabling efficient text search capabilities.

# Create a text index for search functionality
mongo.db.jokes.create_index([
    ("joke_title", TEXT),
    ("joke_description", TEXT),
    ("joke_teller", TEXT)
])



# Pagination
# credit to Ed B, whose code I referenced
# https://github.com/Edb83/self-isolution/blob/master/app.py
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


def get_age():
    """calculates user's age"""

    # default user's age
    user_age = -1
    # if the user is signed in
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

        # assign user's age to user_age, return for use in other views
        user_age = calculate_age(dob)
        return user_age
    else:
        # if the user is not signed in, user_age is -1
        # this ensures user will have only restricted access to site
        # see jokes.html for more information
        user_age == -1
        return user_age


@app.route("/")
@app.route("/get_jokes")
def get_jokes():
    """gets all jokes, age appropriate jokes, renders jokes.html"""

    # if joke is liked, like button is styled with CSS "liked" class
    like_button = "liked"

    # if joke is favourited, favourite button is styled with CSS "liked" class
    favd_button = "favd"

    # get user's age from get_age()
    user_age = get_age()

    # find all favourites from user_favourites collection in MongoDB
    fav_jokes = list(mongo.db.user_favourites.find())

    # if the user is over 18, all jokes are available to them
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
            like_button=like_button,
            favd_button=favd_button
            )
        # if the user is under 18, only age appropriate jokes are available
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
            like_button=like_button,
            favd_button=favd_button
            )


@app.route("/get_users")
def get_users():
    """gets all users from the db"""

    # find all users from users collection in MongoDB
    users = list(mongo.db.users.find())

    # pagination of jokes
    users_paginated = paginated(users)
    pagination = pagination_args(users)

    # render users.html template, pass variables into it
    return render_template(
        "users.html",
        users=users_paginated,
        pagination=pagination
        )


@app.route("/delete_user/<user_id>")
def delete_user(user_id):
    """deletes selected user from db"""

    # remove user from the database
    mongo.db.users.remove({"_id": ObjectId(user_id)})

    # confirmation message
    flash("User removed")

    return redirect(url_for("get_users"))


@app.route("/search", methods=["GET", "POST"])
def search():
    """takes search word from input, displays list of jokes with that word"""

    # retrieve the search word from the form
    search = request.form.get("search")

    # get user's age from get_age()
    user_age = get_age()

    # if the user is over 18, all jokes are available to them
    if int(user_age) >= 18:
        # find all docs with search word from jokes collection in MongoDB
        jokes = list(mongo.db.jokes.find({"$text": {"$search": search}}))

        # pagination of jokes
        jokes_paginated = paginated(jokes)
        pagination = pagination_args(jokes)

        # render jokes.html template, pass jokes variable into it
        return render_template(
            "jokes.html",
            jokes=jokes_paginated,
            user_age=user_age,
            pagination=pagination
            )
        # if the user is under 18, only age appropriate jokes are available
    else:
        age_app_jokes = []

        # find all docs from jokes collection in MongoDB
        jokes = list(mongo.db.jokes.find({"$text": {"$search": search}}))

        # find jokes that are suitable for children
        for joke in jokes:
            if joke["for_children"] == "on":
                age_app_jokes.append(joke)

        # pagination of age_app_jokes
        age_app_jokes_paginated = paginated(age_app_jokes)
        pagination = pagination_args(age_app_jokes)

        # render jokes.html template, pass jokes variable into it
        return render_template(
            "jokes.html",
            user_age=user_age,
            age_app_jokes=age_app_jokes_paginated,
            pagination=pagination
            )


@app.route("/search_users", methods=["GET", "POST"])
def search_users():
    """takes search word from input, displays list of jokes with that word"""

    # retrieve the search word from the form
    search = request.form.get("search")

    # find all docs with search word from users collection in MongoDB
    users = list(mongo.db.users.find({"$text": {"$search": search}}))

    # pagination of users
    users_paginated = paginated(users)
    pagination = pagination_args(users)

    # render jokes.html template, pass jokes variable into it
    return render_template(
        "users.html",
        users=users_paginated,
        pagination=pagination
        )


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    """signs a user up"""

    # if request is POST, sign user up
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

        # insert dictionary into database
        mongo.db.users.insert_one(sign_up)

        # put new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        # confirmation message
        flash("You're signed up!")
        # redirect user to their profile
        return redirect(url_for(
            "profile", username=session["user"]))

    # if request is GET, render sign up form
    return render_template("sign_up.html")


@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
    """signs a user in"""

    # if request is POST, sign user in
    if request.method == "POST":
        # check mongodb for input username
        user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # if username exists, check if input password matches hashed password
        if user:
            # check if input password matches user's password in the database
            if check_password_hash(
                user["password"], request.form.get(
                    "password")):
                session["user"] = request.form.get("username").lower()
                # if passwords match, put user into session
                flash("Welcome, {}!".format(request.form.get("username")))
                # redirect user to their profile
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

    # if request is GET, render sign in form
    return render_template("sign_in.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """displays user's profile, own jokes, and favourite jokes"""

    # if joke is liked, like button styled is with CSS "liked" class
    like_button = "liked"

    # if joke is favourited, favourite button is styled with CSS "favd" class
    favd_button = "favd"

    # set username variable equal to username of session user
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    # initialise list for user's favourite jokes
    fav_jokes = []

    # find all docs from jokes collection in MongoDB
    jokes = list(mongo.db.jokes.find())

    # find all jokes that user has favourited
    for joke in jokes:
        # find the "favouriter" field in each db joke
        favourites = joke["favouriter"]
        if session["user"] in favourites:
            # if so, insert joke into fav_jokes list
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
            pagination=pagination,
            like_button=like_button,
            favd_button=favd_button
            )


@app.route("/add_fav/<joke_id>", methods=["GET", "POST"])
def add_fav(joke_id):
    """allows user to add joke to / remove joke from their favourites"""

    # search jokes for joke passed into view
    joke = mongo.db.jokes.find_one({"_id": ObjectId(joke_id)})

    # get the list of users who favourited the joke
    favouriter_list = joke["favouriter"]

    # loop through list to check if user has already liked the joke
    if session["user"] in favouriter_list:
        # if user's name is in the list,
        # not_favourited is False, otherwise it's True
        not_favourited = False
    else:
        not_favourited = True

    # if the user hasn't favourited the joke, add user's
    # name to list of users who favourited the joke
    if not_favourited:
        # insert user's name into the favouriter_list list
        favouriter_list.append(session['user'])

        # update list in db
        mongo.db.jokes.update_one(
            {"_id": ObjectId(joke_id)},
            {"$set": {"favouriter": favouriter_list}})

        # confirmation message
        flash("Joke favourited!")

        # redirect user to home
        return redirect(url_for("get_jokes"))

    # if user has favourited the joke
    else:
        # remove user's name from list
        favouriter_list.remove(session["user"])

        # update list in db
        mongo.db.jokes.update_one(
            {"_id": ObjectId(joke_id)},
            {"$set": {"favouriter": favouriter_list}})

        # confirmation message
        flash("Joke removed from your favourites")

        # redirect user to home
        return redirect(url_for("get_jokes"))

    # render jokes.html
    return render_template("jokes.html")


@app.route("/like_joke/<joke_id>", methods=["GET", "POST"])
def like_joke(joke_id):
    """allows user to like and unlike a joke"""
    # search users for joke passed into view
    joke = mongo.db.jokes.find_one({"_id": ObjectId(joke_id)})

    # determine how many like the joke currently has
    prev_likes = joke["likes"]

    # get the list of users who like the joke
    liked_by_list = joke["liked_by"]

    # loop through list to check if user has already liked the joke
    if session["user"] in liked_by_list:
        # if user's name is in the list,
        # not_liked is False, otherwise it's True
        not_liked = False
    else:
        not_liked = True

    # if the user hasn't liked the joke, add user's
    # name to list of users who liked the joke
    # increment the joke's likes by 1
    if not_liked:
        # insert user's name into the liked_by list
        liked_by_list.append(session['user'])

        # increment joke's likes by 1
        new_likes = int(prev_likes) + 1

        # update list in db
        mongo.db.jokes.update_one(
            {"_id": ObjectId(joke_id)},
            {"$set": {"liked_by": liked_by_list}})

        # update "likes" in db
        mongo.db.jokes.update_one(
            {"_id": ObjectId(joke_id)},
            {"$set": {"likes": new_likes}})

        # confirmation message
        flash("You've liked this joke!")

        # redirect user to home
        return redirect(url_for("get_jokes"))

    # if user has liked the joke
    else:
        # remove user's name from the liked_by list
        liked_by_list.remove(session["user"])

        # decrement joke's likes by 1
        new_likes = prev_likes - 1

        # update list in db
        mongo.db.jokes.update_one(
            {"_id": ObjectId(joke_id)},
            {"$set": {"liked_by": liked_by_list}})

        # update "likes" in db
        mongo.db.jokes.update_one(
            {"_id": ObjectId(joke_id)},
            {"$set": {"likes": new_likes}})

        # confirmation message
        flash("You've unliked this joke")

        # redirect user to home
        return redirect(url_for("get_jokes"))

    # render jokes.html template
    return render_template("jokes.html")


@app.route("/sign_out")
def sign_out():
    """signs user out"""

    # remove user from session cookies
    session.pop("user")

    # confirmation message
    flash("Signed out")

    # redirect user to sign in form
    return redirect(url_for("sign_in"))


@app.route("/add_joke", methods=["GET", "POST"])
def add_joke():
    """allows user to add a joke to the db"""

    # if request is POST, add joke to db
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
        # confirmation message
        flash("Joke Added!")
        # redirect user to add joke form
        return redirect(url_for("add_joke"))

    # if request is GET, render the add joke form
    return render_template("add_joke.html")


@app.route("/edit_joke/<joke_id>", methods=["GET", "POST"])
def edit_joke(joke_id):
    """allows user to edit their jokes"""

    # find joke by id key in db
    joke = mongo.db.jokes.find_one({"_id": ObjectId(joke_id)})

    # if request is POST, edit the joke in the bd
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
        # confirmation messsage
        flash("Joke Edited!")
        # redirect user to home
        return redirect(url_for("get_jokes"))

    # if request is POST, render edit joke form, with original joke details
    return render_template(
        "edit_joke.html",
        joke=joke
        )


@app.route("/delete_joke/<joke_id>")
def delete_joke(joke_id):
    """allows user to delete their jokes"""

    # remove joke from db
    mongo.db.jokes.remove({"_id": ObjectId(joke_id)})
    # confirmation message
    flash("Joke removed")
    # redirect user to home
    return redirect(url_for("get_jokes"))


@app.errorhandler(404)
def error_not_found(error):
    """handles 404 errors"""

    # if a 404 error occuers, render 404.html
    return render_template("404.html", error=error), 404


@app.errorhandler(500)
def server_error(error):
    """handles 500 errors"""
    # if a 500 error occuers, render 500.html
    return render_template("500.html", error=error), 500


# tell app how and where to run application
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT", 5000)),
            # set to false prior to submission
            debug=False)
