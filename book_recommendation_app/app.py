from flask import Flask, render_template, request
import requests
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///feedback.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    author = db.Column(db.String(100))
    liked = db.Column(db.Boolean)  # True = Like, False = Dislike


GENRES = ["fantasy", "science_fiction", "romance", "mystery", "horror", "historical_fiction"]

@app.route("/")
def index():
    return render_template("index.html", genres=GENRES)

@app.route("/recommend", methods=["POST"])
def recommend():
    keyword = request.form["keyword"]
    url = f"https://openlibrary.org/search.json?q={keyword}&limit=10"
    res = requests.get(url)
    data = res.json()

    books = []
    for doc in data.get("docs", []):
        books.append({
            "title": doc.get("title", "Unknown Title"),
            "author": ", ".join(doc.get("author_name", ["Unknown Author"])),
            "cover_url": f"https://covers.openlibrary.org/b/id/{doc['cover_i']}-L.jpg" if doc.get("cover_i") else None
        })

    return render_template("recommend.html", books=books, genre=keyword)
@app.route("/feedback", methods=["POST"])
def feedback():
    title = request.form["title"]
    author = request.form["author"]
    liked = bool(int(request.form["liked"]))

    fb = Feedback(title=title, author=author, liked=liked)
    db.session.add(fb)
    db.session.commit()

    return "Thanks for your feedback! <a href='/'>Go back</a>"


if __name__ == "__main__":
    app.run(debug=True)
