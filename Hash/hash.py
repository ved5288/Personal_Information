#all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify
from contextlib import closing

# create our application
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def home():
	return render_template('home.html')



@app.route('/ajax')
def ajax_request():
	number =request.form['number']
	return jsonify(number=number) 

if __name__=='__main__':
	app.run(debug=True)
