from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def welcome():
	return render_template('search.html')

@app.route("/Go/<num>")
def go(num=None):
	return render_template('Go',num=int(num)*100)

@app.route("/Square/<num>")
def square(num=None):
	return render_template('Square',num=int(num)*100)


if __name__ == "__main__":
    app.run()
