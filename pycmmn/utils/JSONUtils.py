# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team

import json
import ujson
import ast

from pycmmn.sftp.PySFTPClient import PySFTPClient


class JSONUtils(object):

    @staticmethod
    def json_loads(**kwargs):
        json_file_name = kwargs["filename"]
        with open(json_file_name, "r") as f:
            json_data = json.loads(f.read())
        return json_data

    @staticmethod
    def json_dumps(**kwargs):
        json_file_name = kwargs["filename"]
        json_data = json.dumps(kwargs["dict_data"])
        with open(json_file_name, "w") as f:
            f.write(json_data)

    @staticmethod
    def ujson_loads(**kwargs):
        json_file_name = kwargs["filename"]
        with open(json_file_name, "r") as f:
            json_data = ujson.loads(f.read())
        return json_data

    @staticmethod
    def ujson_dumps(**kwargs):
        json_file_name = kwargs["filename"]
        json_data = ujson.dumps(kwargs["dict_data"])
        with open(json_file_name, "w") as f:
            f.write(json_data)

    @staticmethod
    def json_load(fp):
        return json.load(fp)

    @staticmethod
    def ujson_load(line):
        return ujson.loads(line)

    @staticmethod
    def ujson_dump(line):
        return ujson.dump(line)

    @staticmethod
    def string_to_dict(line):
        return ast.literal_eval(line)

    @staticmethod
    def read_sftp_json_from_file(sftp_client: PySFTPClient, filename: str):
        f = sftp_client.open(filename, "r")
        result_dict = json.loads(f.read())
        f.close()
        return result_dict


if __name__ == '__main__':
    pass
