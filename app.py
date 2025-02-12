from flask import Flask, render_template

app = Flask(__name__)

from aulas.aula_1.main import aula1_bp
from aulas.aula_2.main import aula2_bp
from aulas.aula_3.main import aula3_bp

app.register_blueprint(aula1_bp, url_prefix="/aula1")
app.register_blueprint(aula2_bp, url_prefix="/aula2")
app.register_blueprint(aula3_bp, url_prefix="/aula3")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/canva")
def canva():
    return render_template("list1_aula3/canva.html")


@app.route("/webcam")
def webcam():
    return render_template("list1_aula3/webcam.html")


@app.route("/list")
def list_page():
    return render_template("list1_aula3/list.html")


@app.route("/menu")
def menu():
    return render_template("list1_aula3/menu.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
