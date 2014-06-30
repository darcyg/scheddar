import json
from scheddar.app import app

app.testing = True

def test_create():
    client = app.test_client()
    res = client.post('/api/running', content_type='application/json', data=json.dumps({'commandline': 'ls'}))
    assert {'result': True} == json.loads(res.data)
