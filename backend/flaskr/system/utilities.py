from random import randint
from cerberus import Validator
from dateutil import parser


class Utilities:
    def __init__(self):
        pass

    @staticmethod
    def rand_string(length=15, chars='ABCDEFGHIJKLMNPQRSTUVWXYZabcdefghqrt123456789', string=''):
        chars_length = (len(chars) - 1)
        if len(string) >= length:
            return string
        string += chars[randint(0, chars_length)]
        if len(string) >= length:
            return string

        for i in range(1, length):
            i = len(string)
            r = chars[randint(0, chars_length)]
            if r != string[i - 1]:
                string += r

        if len(string) < length:
            return Utilities.rand_string(length, chars, string)
        return string

    @staticmethod
    def validate(schema, request):
        v = Validator(schema)
        status = v.validate(request)
        if not status:
            return v.errors
        else:
            return None

    @staticmethod
    def validate_meta(metadata, allowed_types):
        data = {}

        for data in metadata:
            data_type = str(data["type"]).lower()

            if data_type not in allowed_types:
                return {"error": data + " can only be a string, number, date or enum"}

            if data["type"] == "date":
                time = parser.parse(data["data"])
                data["data"] = time.strftime('%Y-%m-%d %H:%M:%S')

        return metadata


