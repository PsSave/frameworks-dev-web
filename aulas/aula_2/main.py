from flask import Blueprint, render_template

aula2_bp = Blueprint("aula2", __name__)


@aula2_bp.route("/")
def index():
    return render_template("aulas/aula2.html")
