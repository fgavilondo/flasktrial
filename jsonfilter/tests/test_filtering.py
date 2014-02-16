import unittest
import json

import jsonfilter.json_filter as jf


class FilteringTestCase(unittest.TestCase):
    def test_filter_valid_request(self):
        f = open("./sample_response.json")
        expected_response = json.load(f)
        f.close()
        json_string = self._read_json_file("./sample_request.json")
        actual_response = jf.filter_string_request(json_string)
        self.assertEqual(expected_response, actual_response)

    def _read_json_file(self, json_file_name):
        with open(json_file_name, "r") as f:
            json_string = f.read()
            return json_string

    def test_filter_invalid_json(self):
        self._assert_error('not json')
        self._assert_error('{}')
        self._assert_error('{"payload"}')
        self._assert_error('{"payload":}')
        self._assert_error('{"payload": [}')
        self._assert_error('{"payload": [{]}')
        self._assert_error('{"payl": [{}]}')

    def _assert_error(self, json_string):
        # this does not seem to work with chained exceptions
        # self.assertRaises(jf.BadJsonException, jf.filter_string_request(json_string))
        try:
            jf.filter_string_request(json_string)
        except jf.BadJsonException:
            pass
        else:
            self.fail("Expected BadJsonException for " + json_string)


if __name__ == '__main__':
    unittest.main()

