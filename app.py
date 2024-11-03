from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'

@app.route('/canva')
def canvas():
    return render_template('canva.html')



if __name__ == '__main__':
    app.run(debug=True)