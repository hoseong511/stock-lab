# pip install Flask Flask-Restful
from flask import Flask
from flask_restful import rqparse, abort, Api, Resource

app = Flask(__name__)