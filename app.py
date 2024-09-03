# imports
from flask import Flask

# defines the app
app = Flask(__name__)

@app.route("/") # basically where the app is hosted

def application():
    return "template"

# runs the app
if __name__ == "__main__":
    app.run()