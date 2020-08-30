from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import pymongo
import dns

load_dotenv()
URI = os.getenv('MONGO_URI')
app = Flask(__name__)

@app.route('/')
def search():
    name = request.args.get('name')
    subject = request.args.get('subject')
    grade = request.args.get('grade')

    def get_tutor(name, subject, grade):
        my_client = pymongo.MongoClient(URI)
        my_db = my_client['touch-tutors']
        my_col = my_db['tutors']
        tutor = my_col.find_one({'subject': str(subject)}, {'grade': str(grade)})

        tutors = {
            'name': tutor['name'],
            'price': tutor['price'],
            'phone': tutor['phone'],
            'description': tutor['description']
        }

    return render_template('search.html')

@app.route('/results')
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run()
