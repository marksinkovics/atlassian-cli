""" Test CustomDateTime property """

from datetime import datetime

from jsonobject import JsonObject
import pytest

from atlassian_cli.helpers import CustomDateTimeProperty

# pylint: disable=R0903

DATETIME_FORMAT = '%Y-%m-%dT%H-%M-%S:%f'

class TestModel(JsonObject):
    """ Class for testing property """
    sample = CustomDateTimeProperty(datetime_format=DATETIME_FORMAT)

# pylint: disable=R0903,R0201
class CustomDateTimePropertyTestCase:
    """ Test epoch property """

    datetime_string = '2000-01-02T11-12-13:140000'
    json_obj = {'sample' : datetime_string}
    wrong_json_obj = {'sample' : '2000;01;02T11;12;13;140000'}
    invalid_json_obj = {'sample' : 1}
    date = datetime(2000, 1, 2, 11, 12, 13, 140000)
    obj = TestModel(json_obj)

    def test_mapping(self):
        """ Test simple mapping """
        result = TestModel(self.json_obj)
        assert result.sample == self.date

    def test_mapping_fail_wrong_json(self):
        """ Test mapping failed """
        with pytest.raises(ValueError):
            _ = TestModel(self.wrong_json_obj)

    def test_mapping_fail_invalid_value(self):
        """ Test mapping failed """
        with pytest.raises(ValueError):
            _ = TestModel(self.invalid_json_obj)

    def test_unmapping(self):
        """ Test simple unmapping """
        result = self.obj.to_json()['sample']
        assert result == self.datetime_string

    def test_unmapping_failed(self):
        """ Test unmapping failed """
        mock_obj = TestModel(self.json_obj)
        with pytest.raises(ValueError):
            mock_obj.sample = 1
