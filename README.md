flasktrial
==========

## Pre-requisites

* Pyhton, pip, virtualenv

## Set-up

1. Create a virtual environment

    `cd flasktrial`

    `virtualenv env`

2. Install project dependencies

    Mac/Linux: env/bin/pip install -r requirements.txt
    
    Windows:   env\Scripts\pip install -r requirements.txt

3. Launch the application with

    `./jsonfilter/app.py`

4. Test the application locally by POSTing some JSON to http://127.0.0.1:5000/api/v1.0/jsonfilter, e.g. with curl

    `curl -i -H "Content-Type: application/json" -X POST -T ./jsonfilter/test/sample_request.json http://127.0.0.1:5000/api/v1.0/jsonfilter`
