from flask import Flask, render_template, request, url_for, session, redirect
from dotenv import load_dotenv
import os
import pymongo
import bcrypt
import dns

load_dotenv()
URI = os.getenv('MONGO_URI')
app = Flask(__name__)

@app.route('/')
def search():
    name = request.args.get('name')
    subject = request.args.get('subject')
    grade = request.args.get('grade')

    
    return render_template('search.html')

@app.route('/results')
def results():
    return render_template('results.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup_tutor', methods=['POST', 'GET'])
def signup_tutor():
    return render_template('signup_tutor.html')

@app.route('/signup_student', methods=['POST', 'GET'])
def signup_student():
    return render_template('signup_student.html')




if __name__ == '__main__':
    app.run()
