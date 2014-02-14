"""
By default, AWS Elastic Beanstalk looks for your application (application.py) in top-level directory of your source bundle.
"""

from flask import Flask
from flask import make_response
from flask import abort
from flask import jsonify
from flask import request
import jsonfilter.json_filter as jf

# By default, AWS Elastic Beanstalk expects the Flask instance to be called 'application'
application = Flask(__name__)


@application.route('/')
def index():
    return 'Nothing to see here.'


@application.route('/api/v1.0/jsonfilter', methods=['POST'])
def filter_json():
    if not request.json:
        abort(400)
    response = jf.filter_request_from_object_return_object(request.json)
    if 'error' in response:
        return jsonify(response), 400
    else:
        return jsonify(response), 200


@application.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Could not decode request'}), error)


if __name__ == '__main__':
    # Set application.debug=true to enable tracebacks on Beanstalk log output.
    # Make sure to remove this line before deploying to production.
    application.run(host='0.0.0.0', debug=False)
