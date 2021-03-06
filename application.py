"""
By default, AWS Elastic Beanstalk looks for your application (application.py) in top-level directory of your source bundle.
"""

from flask import Flask
from flask import make_response
from flask import abort
from flask import jsonify
from flask import request
import werkzeug
import jsonfilter.json_filter as jf


# By default, AWS Elastic Beanstalk expects the Flask instance to be called 'application'
application = Flask(__name__)

# Load default config and override config from an environment variable
application.config.update(dict(
    DEBUG=False
))
application.config.from_envvar('APP_SETTINGS', silent=True)


@application.route('/')
def index():
    return 'Nothing to see here.'


@application.route('/api/v1.0/jsonfilter', methods=['POST'])
def filter_json():
    try:
        json_object = request.get_json()
    except werkzeug.exceptions.BadRequest:
        abort(400)
    else:  # all good so far
        try:
            result = jf.filter_json_request(json_object)
        except jf.BadJsonException:
            abort(400)
        else:
            json_response = jsonify(result)
            return json_response, 200


@application.errorhandler(400)
def bad_request(error):
    """
    Modify 400 error handler to respond with JSON (instead of HTML default)
    """
    return make_response(jsonify({'error': 'Could not decode request'}), 400)


if __name__ == '__main__':
    # Set application.debug=true to enable tracebacks on Beanstalk log output.
    # Make sure to remove this line before deploying to production.
    # Even though the interactive debugger does not work in forking environments (which makes it nearly impossible to use on production servers), it still allows the execution of arbitrary code.
    # This makes it a major security risk and therefore it must never be used on production machines.
    application.run(host='0.0.0.0')
