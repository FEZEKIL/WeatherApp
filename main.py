from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/")
def about():
    return render_template("api/v1<station><date>")

app.run(debug=True)