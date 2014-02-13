#!env/bin/python

"""
By default, AWS Elastic Beanstalk looks for your application (application.py) in top-level directory of your source bundle.
"""

from flask import Flask
from flask import make_response
from flask import abort
from flask import jsonify
from flask import request
import jsonfilter.json_filter as jf

app = Flask(__name__)


@app.route('/')
def index():
    return 'Nothing to see here.'


@app.route('/api/v1.0/jsonfilter', methods=['POST'])
def filter_json():
    if not request.json:
        abort(400)
    response = jf.filter_request_from_object_return_object(request.json)
    if 'error' in response:
        return jsonify(response), 400
    else:
        return jsonify(response), 200


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Could not decode request'}), error)


if __name__ == '__main__':
    app.run(debug=True)
