""" Action for argparse """

import argparse

# pylint: disable=R0903

class NonEmptyStringAction(argparse.Action):
    """ Validate arguments is empty string or not """
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super().__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        if not values:
            raise ValueError("Empty string")
        setattr(namespace, self.dest, values)
