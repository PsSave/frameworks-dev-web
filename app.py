from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('menu.html')

@app.route('/canva')
def canvas():
    return render_template('canva.html')

@app.route('/webcam')
def webcam():
    return render_template('webcam.html')

@app.route('/list')
def list():
    return render_template('list.html')

if __name__ == '__main__':
    app.run(debug=True)