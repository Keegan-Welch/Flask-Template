# imports
from flask import Flask, render_template

# defines the app
app = Flask(__name__)

@app.route("/") # host

def application():
    return render_template("index.html")

# runs the app
if __name__ == "__main__":
    app.run()