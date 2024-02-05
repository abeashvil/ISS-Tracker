#main.py

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__,
            template_folder="C:/Users/thesl/Desktop/ISS-Tracker/templates")

@app.route("/")
def home():
    return render_template("homepage.html")



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

