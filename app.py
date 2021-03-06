from flask import Flask, render_template, request
from flask_cors import CORS
import models

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET", "POST"])
def index():
    models.create_db()
    if request.method == "GET":
        pass

    if request.method == "POST":
        name = request.form.get("name")
        post = request.form.get("post")
        models.create_post(name, post)

    posts = models.get_posts()
    return render_template("index.html", posts = posts)
