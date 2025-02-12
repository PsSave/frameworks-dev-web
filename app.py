from flask import Flask, render_template

app = Flask(__name__)

from aulas.aula_1.main import aula1_bp
from aulas.aula_2.main import aula2_bp

app.register_blueprint(aula1_bp, url_prefix="/aula1")
app.register_blueprint(aula2_bp, url_prefix="/aula2")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
