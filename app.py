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

    def get_tutor(subject, grade):
        my_client = pymongo.MongoClient(URI)
        my_db = my_client['touch-tutors']
        my_col = my_db['tutors']
<<<<<<< Updated upstream
        tutor = my_col.find_one({'subject': str(subject)}, {'grade': str(grade)})

        tutors = {
            'name': tutor['name'],
            'price': tutor['price'],
            'phone': tutor['phone'],
            'description': tutor['description']
        }

        return tutors
      
    output = get_tutor(name, subject, grade)
    return render_template('results.html', name=output['name'], price=output['price'], phone=output['phone'], description=output['description'])
=======
        tutor = my_col.find({'subject': str(subject)}, {'grade': str(grade)})
        return tutor

    output = get_tutor(subject, grade)
    name = output['name']
    return render_template('results.html', name=name)
>>>>>>> Stashed changes


@app.route('/job-posting')
def job():
    return render_template('job_post.html')


if __name__ == '__main__':
    app.run()
