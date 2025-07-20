from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host="185.105.89.195", port="8080", debug=True)
