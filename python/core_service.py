from __future__ import print_function

import json
import pathlib

from python.schooldata import SchoolData

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    # Python 2.x fallback
    from argparse import Namespace


# https://pynative.com/python-convert-json-data-into-custom-python-object/

class CoreService(object):

    # only for testing purposes
    @classmethod
    def get_processed_json(cls, json_string: str) -> SchoolData:
        obj = json.loads(json_string, object_hook=lambda d: Namespace(**d))
        return SchoolData(obj.classes, obj.teachers, obj.subjects, obj.constraints)


    @classmethod
    def read_json(cls, file: str) -> str:
        data: str = None
        with open(pathlib.Path(__file__).parent / file, 'r') as myfile:
            data =myfile.read()
        return data




