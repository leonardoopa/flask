from flask import Flask, render_template


app = Flask(__name__)

@app.route('/inicio')
def ola_mundo():
    return render_template('lista.html')


if __name__ == '__main__':
    app.run()