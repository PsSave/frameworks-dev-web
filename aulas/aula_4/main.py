from flask import Blueprint, render_template

aula4_bp = Blueprint("aula4", __name__)


@aula4_bp.route("/")
def index():
    return render_template("aulas/aula4.html")
