from flask import Flask, render_template

app = Flask(__name__)
#home
@app.route("/")
def home():
    return render_template("home.html", active_page="home")
#about
@app.route("/about")
def about():
    return render_template("about.html", active_page="about")
#Projects
@app.route("/projects")
def projects():
    return render_template("projects.html", active_page="projects")
#photos
@app.route("/photos")
def photos():
    return render_template("photos.html", active_page="photos")
#videos
@app.route("/videos")
def videos():
    return render_template("videos.html", active_page="videos")
#contacts
@app.route("/contacts")
def contacts():
    return render_template("contacts.html", active_page="contacts")

if __name__ == "__main__":
    app.run(debug=True)
