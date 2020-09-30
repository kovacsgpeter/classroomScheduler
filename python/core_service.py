from __future__ import print_function

import json

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
    def read_json(cls, file: str) -> str:

        # read file
        with open(file, 'r') as myfile:
            data = myfile.read()
        #studentJsonData = json.dumps(data, indent=4, cls=SchoolDataEncoder)
        #json.loads(studentJsonData, object_hook=lambda d: Namespace(**d))
        # x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        x = json.loads(data, object_hook=lambda d: Namespace(**d))
        # y = json.loads(data.replace("\n", "").replace(" ", ""),
        #            object_hook=object_decoder)
        return object_decoder(x)
        # parse file
        # obj = json.loads(data)

# class User(object):
#     def __init__(self, name, username):
#         self.name = name
#         self.username = username
#
# import json
def object_decoder(obj) -> SchoolData:
    return SchoolData(obj.classes, obj.teachers, obj.subjects, obj.constraints)

# json.loads('{"__type__": "User", "name": "John Smith", "username": "jsmith"}',
#            object_hook=object_decoder)
#
# print type(User)  # -> <type 'type'>



