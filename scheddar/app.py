from flask import Flask
from flask.ext.restful import Api, Resource
import scheddar.api.running

app = Flask(__name__)
api = Api(app)


api.add_resource(scheddar.api.running.RunningTasks, '/api/running', endpoint='running')

