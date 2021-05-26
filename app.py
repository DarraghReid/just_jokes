import os
from flask import Flask
# need to import env package in order to use environment variables
# import env only if the os can find an existing file path for
# the env.py path itself (not pushed, Heroku won't be able to find it)
if os.path.exists("env.py"):
    import env


# create instance of Flask in variable 'app'
app = Flask(__name__)


# test if app is configured
# "/" is the default route
@app.route("/")
def test():
    return "Hello, World"


# tell app how and where to run application
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            # set to false prior to submission
            debug=True)
