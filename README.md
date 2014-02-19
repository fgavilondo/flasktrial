flasktrial
==========

# Building and testing the application

## Pre-requisites

* Pyhton, pip, virtualenv

## Steps

1. Create a virtual environment

    `cd flasktrial`

    `virtualenv env`

1a. Ensure you are in the virtualenv by using `source env/bin/activate` on unixes and `env\Scripts\activate.bat` on Windows.

2. Install project dependencies

    `pip install -r requirements.txt`

3. Run the tests

    `nosetests -v`

4. Launch the application locally

    `python application.py`

5. Check the application locally by POSTing some JSON to http://127.0.0.1:5000/api/v1.0/jsonfilter, e.g. with curl

    Good request: `curl -i -H "Content-Type: application/json" -X POST -T jsonfilter/tests/sample_request.json http://127.0.0.1:5000/api/v1.0/jsonfilter`

    Bad request: `curl -i -H "Content-Type: application/json" -X POST -d "notjson" http://127.0.0.1:5000/api/v1.0/jsonfilter`


# Deploying to AWS Elastic Beanstalk

2 options:

### Using the Elastic Beanstalk web console

Steps:

http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_python_console.html

### Using Eb (the AWS Elastic Beanstalk Command Line Tool)

Pre-requisites:

* Elastic Beanstalk command line tools. Get package from the AWS Sample Code & Libraries website (http://aws.amazon.com/code/6752709412171743)
* Git 1.6.6 or later
* Python 2.7 or 3.0

See http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_Python_flask.html

But essentially: 

* run 'eb init' once
* run 'eb start' once
* run 'eb status --verbose' and note down the URL (The application is available at http://[EB Environment Name].elasticbeanstalk.com/api/v1.0/jsonfilter)
* from then on just 'git commit' your changes and run 'git aws.push' to update the app on AWS
* run 'eb logs' for diagnosing problems

Eventually:

* 'eb stop'
* 'eb delete'
