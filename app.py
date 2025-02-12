from flask import Flask, render_template, request, session, jsonify

app = Flask(__name__)

from aulas.aula_1.main import aula1_bp
from aulas.aula_2.main import aula2_bp
from aulas.aula_3.main import aula3_bp
from aulas.aula_4.main import aula4_bp

app.register_blueprint(aula1_bp, url_prefix="/aula1")
app.register_blueprint(aula2_bp, url_prefix="/aula2")
app.register_blueprint(aula3_bp, url_prefix="/aula3")
app.register_blueprint(aula4_bp, url_prefix="/aula4")

app.secret_key = "minha_chave_secreta"


class Pessoa:
    def __init__(self, username, password, nome):
        self.username = username
        self.password = password
        self.nome = nome

    def authenticate(self, username, password):
        return self.username == username and self.password == password


usuario_teste = Pessoa("teste", "1234", "João")

templates_generated = {}


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


@app.route("/aula4atv1")
def atv1():
    if "attempts" not in session:
        session["attempts"] = 0

    message = ""
    if request.method == "POST":
        if session["attempts"] >= 2:
            message = "Número máximo de tentativas atingido."
        else:
            username = request.form.get("username")
            password = request.form.get("password")
            if usuario_teste.authenticate(username, password):
                message = f"Bom dia {usuario_teste.nome}"
                session["attempts"] = 0
            else:
                session["attempts"] += 1
                message = "Usuário e senha não conferem."
    return render_template("list2_aula4/auth.html", message=message)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
