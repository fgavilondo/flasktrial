import unittest
import json

import jsonfilter.json_filter as jf


class TestJsonFilter(unittest.TestCase):
    def test_filter_valid_request(self):
        f = open("./sample_response.json")
        expected_response = json.load(f)
        f.close()
        actual_response = jf.filter_request_from_file_return_object("./sample_request.json")
        self.assertEqual(expected_response, actual_response)

    def test_filter_invalid_json(self):
        error_str = jf.filter_request_from_string_return_string("not json")
        self.assertEqual('{"error": "Could not decode request"}', error_str)
