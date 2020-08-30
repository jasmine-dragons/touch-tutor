from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import pymongo
import dns

load_dotenv()
app = Flask(__name__)

@app.route('/')
return render_template('search.html')


if __name__ == '__main__':
    app.run()
