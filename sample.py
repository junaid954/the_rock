from flask import Flask, templating
app = Flask ("chacha")
@app.route("/home/")
def home ():
    return templating.render_template("index.html")
