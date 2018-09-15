""" Test epoch property """

from datetime import datetime

from jsonobject import JsonObject
import pytest

from atlassian_cli.helpers import EpochProperty

# pylint: disable=R0903

class EpochPropertySample(JsonObject):
    """ Class for testing property """
    sample = EpochProperty()

# pylint: disable=R0201
class EpochPropertyTestCase:
    """ Test epoch property """

    epochTime = 946782245000
    json_obj = {'sample' : 946782245000}
    wrong_json_obj = {'sample' : '946782245000'}
    invalid_iso_json_obj = {'sample' : 946782245000000}
    date = datetime(2000, 1, 2, 3, 4, 5, 0)
    obj = EpochPropertySample({'sample' : 946782245000})

    def test_mapping(self):
        """ Test simple mapping """
        result = EpochPropertySample(self.json_obj)
        assert result.sample == self.date

    def test_mapping_fail(self):
        """ Test mapping failed """
        with pytest.raises(ValueError):
            _ = EpochPropertySample(self.json_obj)

    def test_mapping_fail_invalid_iso(self):
        """ Test mapping failed """
        with pytest.raises(ValueError):
            _ = EpochPropertySample(self.invalid_iso_json_obj)

    def test_unmapping(self):
        """ Test simple unmapping """
        result = self.obj.to_json()['sample']
        assert result == self.epochTime

    def test_unmapping_failed(self):
        """ Test unmapping failed """
        mock_obj = EpochPropertySample({'sample' : 946782245000})
        with pytest.raises(ValueError):
            mock_obj.sample = 1
