from flask import Flask

#create app object as an instance of the Flask class
app = Flask(__name__)

from app import routes
