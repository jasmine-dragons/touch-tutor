from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import pymongo
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
    location = request.args.get('location')

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


if __name__ == '__main__':
    app.run()
