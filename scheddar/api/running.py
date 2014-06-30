from flask.ext import restful
from flask.ext.restful import reqparse


class RunningTasks(restful.Resource):
    def __init__(self, *args, **kwargs):
        super(RunningTasks, self).__init__(*args, **kwargs)
        parser = reqparse.RequestParser()
        parser.add_argument('commandline', type=str, required=True, help='No command line specified', location='json')
        self.args = parser.parse_args()

    def post(self):
        print self.args['commandline']
        return {'result': True}
