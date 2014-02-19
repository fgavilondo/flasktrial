import unittest

import application


class ApplicationTestCase(unittest.TestCase):
    def setUp(self):
        application.application.config['TESTING'] = True
        self.client = application.application.test_client()

    def test_index(self):
        """Should say 'Nothing to see here' on index page"""
        # if we use docstrings in our tests nosetests will display them instead of the fixture/test case name.
        # personally i don't find that very useful, i prefer to see the test names.
        response = self.client.get('/')
        self.assertEqual("200 OK", response.status)
        self.assertTrue("Nothing to see here" in response.data)

    def test_filter_invalid_json(self):
        response = self.client.post('/api/v1.0/jsonfilter', data='aaa')
        self.assertEqual("400 BAD REQUEST", response.status)
        self.assertTrue("Could not decode request" in response.data)

        response = self.client.post('/api/v1.0/jsonfilter', data='{}')
        self.assertEqual("400 BAD REQUEST", response.status)
        self.assertTrue("Could not decode request" in response.data)

    def test_filter_correct_json(self):
        json_string = self._read_file("./jsonfilter/tests/sample_request.json")
        response = self.client.post('/api/v1.0/jsonfilter',
                                    headers=[('Content-Type', 'application/json')],
                                    data=json_string)
        self.assertEqual("200 OK", response.status)
        self.assertTrue("response" in response.data)

    def _read_file(self, json_file_name):
        with open(json_file_name, "r") as f:
            return f.read()


if __name__ == '__main__':
    unittest.main()
