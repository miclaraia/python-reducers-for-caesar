import unittest
from panoptes_aggregation.reducers import process_kwargs


class TestProcessKwargs(unittest.TestCase):
    def setUp(self):
        self.DEFAULTS = {
            'a': {'default': 5.0, 'type': float},
            'b': {'default': 3, 'type': int},
            'c': {'default': 'hi', 'type': str},
        }

    def test_defaults(self):
        kwargs = {}
        expected = {
            'a': 5.0,
            'b': 3,
            'c': 'hi'
        }
        self.assertDictEqual(process_kwargs(kwargs, self.DEFAULTS), expected)

    def test_setting_value(self):
        # make sure value sets as correct type
        kwargs = {'a': '10'}
        expected = {
            'a': 10.0,
            'b': 3,
            'c': 'hi'
        }
        self.assertDictEqual(process_kwargs(kwargs, self.DEFAULTS), expected)

    def test_wrong_type(self):
        # make sure default is used with bad keywords are passed in
        kwargs = {'b': '10.5'}
        expected = {
            'a': 5.0,
            'b': 3,
            'c': 'hi'
        }
        self.assertDictEqual(process_kwargs(kwargs, self.DEFAULTS), expected)

    def test_wrong_key(self):
        # make sure invalid keywords are not passed in
        kwargs = {'random': 'set'}
        expected = {
            'a': 5.0,
            'b': 3,
            'c': 'hi'
        }
        self.assertDictEqual(process_kwargs(kwargs, self.DEFAULTS), expected)


if __name__ == '__main__':
    unittest.main()
