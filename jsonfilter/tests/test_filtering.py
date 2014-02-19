import unittest
import json

import os
import jsonfilter.json_filter as jf


def absolute_file_path(relative_path):
    return os.path.join(os.path.dirname(__file__), relative_path)


class FilteringTestCase(unittest.TestCase):
    def test_filter_valid_request(self):
        with open(absolute_file_path("sample_response.json")) as f:
            expected_response = json.load(f)
            json_string = self._read_json_file(absolute_file_path("sample_request.json"))
            actual_response = jf.filter_string_request(json_string)
            self.assertEqual(expected_response, actual_response)

    def _read_json_file(self, json_file_name):
        with open(json_file_name, "r") as f:
            json_string = f.read()
            return json_string

    def test_filter_invalid_json(self):
        """Should error for an invalid request"""
        # if we use docstrings in our tests nosetests will display them instead of the fixture/test case name.
        # personally i don't find that very useful, i prefer to see the test names.
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

