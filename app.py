from flask import Flask, render_template, request, url_for, session, redirect
from dotenv import load_dotenv
import os
import pymongo
import bcrypt
import dns
import json

load_dotenv()
URI = os.getenv('MONGO_URI')
app = Flask(__name__)


@app.route('/')
def search():
    return render_template('search.html')


@app.route('/results')
def results():
    name = request.args.get('name')
    subject = request.args.get('subject')
    grade = request.args.get('grade')


    def get_tutor(subject, grade):
        my_client = pymongo.MongoClient(URI)
        my_db = my_client['touch-tutors']
        my_col = my_db['tutors']
        tutor = my_col.find_one({'subject': str(subject)}, {'grade': str(grade)})
        return tutor

    output = get_tutor(subject, grade)
    name = output['names']
    return render_template('results.html', name=name)


@app.route('/job-posting')
def job():
    return render_template('job_post.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/ourtutors')
def ourtut():
    return render_template('ourTutors.html')



@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup_tutor', methods=['POST', 'GET'])
def signup_tutor():
    return render_template('signup_tutor.html')

@app.route('/signup_student', methods=['POST', 'GET'])
def signup_student():
    return render_template('signup_student.html')

@app.route('/register_tutor')
def getValuesTutor():
    Name = request.args.get('name')
    Price = request.args.get('price')
    Phone = request.args.get('phone')
    Description = request.args.get('description')

    values = [
        Name,
        Price,
        Phone,
        Description
    ]

    my_client = pymongo.MongoClient('mongodb+srv://tutor:applebanana@cluster0.5tibu.mongodb.net/touch-tutor?retryWrites=true&w=majority')
    my_db = my_client['touch-tutor']
    my_col = my_db['tutors']
    my_col.insert_one({Name, Price, Phone, Description})

    return render_template('/search.html')




if __name__ == '__main__':
    app.run()
