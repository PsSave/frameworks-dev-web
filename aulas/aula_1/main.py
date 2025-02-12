from flask import Blueprint, render_template

aula1_bp = Blueprint("aula1", __name__)


@aula1_bp.route("/")
def index():
    return render_template("aulas/aula1.html")
