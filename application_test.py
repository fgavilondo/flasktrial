import unittest

import application


class ApplicationTestCase(unittest.TestCase):
    def setUp(self):
        application.application.config['TESTING'] = True
        self.client = application.application.test_client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual("200 OK", response.status)
        assert b'Nothing to see here' in response.data

    def test_filter_invalid_json(self):
        response = self.client.post('/api/v1.0/jsonfilter', data=dict(
            json='aaa'))
        self.assertEqual("400 BAD REQUEST", response.status)
        assert b'Could not decode request' in response.data

        response = self.client.post('/api/v1.0/jsonfilter', data=dict(
            json='{}'))
        self.assertEqual("400 BAD REQUEST", response.status)
        assert b'Could not decode request' in response.data

    def test_filter_correct_json(self):
        # TODO fix this test, the request does not seem to be set up correctly
        json_string = self._read_json_file("./jsonfilter/tests/sample_request.json")
        response = self.client.post('/api/v1.0/jsonfilter',
                                    headers=[('Content-Type', 'application/json')],
                                    data=dict(json=json_string))
        self.assertEqual("200 OK", response.status)
        assert b'response' in response.data

    def _read_json_file(self, json_file_name):
        with open(json_file_name, "r") as f:
            json_string = f.read()
            return json_string


if __name__ == '__main__':
    unittest.main()
