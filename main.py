from flask import Flask, render_template

app = Flask (__name__)

#request, ki pride sem: /
#response: Hello world

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/hello-msg/<name>")
def hello_stranger(name):
    return f"Hello {name}"

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/portfolio.html")
def portfolio():
    return render_template("portfolio.html")



if __name__ == "__main__":
    app.run(port=3000)

