from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/aboutme")
def aboutme():
    return render_template('aboutme.html')

@app.route("/skills")
def skills():
    return render_template('skills.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')

@app.route("/contactme")
def contactme():
    return render_template('contactme.html')

if __name__ =="__main__":
    app.run(debug=True)