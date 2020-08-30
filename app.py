from flask import Flask, render_template, request, url_for, session, redirect, jsonify
from dotenv import load_dotenv
import os
import pymongo
import bcrypt
import dns
import json
from bson.objectid import ObjectId
from bson.json_util import dumps, loads


load_dotenv()
URI = os.getenv('MONGO_URI')
app = Flask(__name__)


@app.route('/')
def search():
    return render_template('search.html')

@app.route('/student_landing')
def student_landing():
    StudentName = request.args.get('name')
    return render_template('student_landing.html', Name = StudentName)

@app.route('/tutor_landing')
def tutor_landing():
    TutorName = request.args.get('name')
    return render_template('tutor_landing.html', Name = TutorName)



@app.route('/results')
def results():
    name = request.args.get('name')
    subject = request.args.get('subject')
    grade = request.args.get('grade')


    def get_tutor(subject, grade):
        my_client = pymongo.MongoClient(URI)
        my_db = my_client['touch-tutor']
        my_col = my_db['postings']
        tutor = my_col.find({'subject': str(subject), 'grade': int(grade)})
        return tutor

    output = get_tutor(subject, grade)

    #tutor_name = loads(dumps(list(output)))
    return render_template('results.html', name=output[0]['name'], price=output[0]['price'], description=output[0]['description'], phone=output[0]['phone'])



@app.route('/job-posting')
def job():
    return render_template('job_post.html')
    
@app.route('/insert-post')
def insert_post():
    Name = request.args.get('name')
    InputSubject = str(request.args.get('input-subject'))
    InputGrade = request.args.get('input-grade')
    UserPrice = request.args.get('user-price')
    UserDescription = str(request.args.get('user-description'))
    PhoneNumber = request.args.get('phone-number')
    

    values = {'subject' : InputSubject, 'grade' : InputGrade, 'price' : UserPrice, 'description' : UserDescription, 'name' : Name, 'phone' : PhoneNumber}

    my_client = pymongo.MongoClient(URI)
    my_db = my_client['touch-tutor']
    my_col = my_db['postings']
    my_col.insert_one(values)

    return render_template('search.html')


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

    values = {'Name' : Name, 'Price' : Price, 'Phone' : Phone, 'Description' : Description}



    my_client = pymongo.MongoClient(URI)
    my_db = my_client['touch-tutor']
    my_col = my_db['tutors']
    my_col.insert_one(values)


    TutorName = request.args.get('name')
    return render_template('/tutor_landing.html', Name = TutorName)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_tutor')
def login_tutor():
    return render_template('login_tutor.html')

@app.route('/login_student')
def login_student():
    return render_template('login_student.html')



if __name__ == '__main__':
    app.run()

