from flask import Blueprint, render_template

aula3_bp = Blueprint("aula3", __name__)


@aula3_bp.route("/")
def index():
    return render_template("aulas/aula3.html")
