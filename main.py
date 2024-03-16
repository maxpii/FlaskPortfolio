from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route('/Calculator')
def calculator():
    return render_template("calculator.html")

@app.route('/Tic-Tac-Toe')
def tic_tac_toe():
    return render_template("tic-tac-toe.html")

@app.route('/Color-Changer')
def color_changer():
    return render_template("color-changer.html")

@app.route("/Clicker")
def clicker():
    return render_template("clicker.html")


