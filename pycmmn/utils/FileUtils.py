# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team
######################################################################################

import os
import shutil
from typing import List, Union

StrPathLike = Union[str, os.PathLike]


class FileUtils(object):
    @staticmethod
    def read_dir(directory: StrPathLike = "./", ext: StrPathLike = ".done"):
        file_names = os.listdir(directory)

        res_file_names = []
        for file_name in file_names:
            if ext == os.path.splitext(file_name)[-1]:
                res_file_names.append(f"{directory}/{file_name}")

        return res_file_names

    @staticmethod
    def mkdir(dir_name: StrPathLike):
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

    @staticmethod
    def get_realpath(file: StrPathLike):
        return os.path.dirname(os.path.realpath(file))

    @classmethod
    def remove_dir(cls, dir_name: StrPathLike):
        if cls.is_exist(dir_name):
            shutil.rmtree(dir_name)

    @staticmethod
    def is_exist(file: StrPathLike):
        return os.path.exists(file)

    @classmethod
    def search_package(cls, dirname: StrPathLike, exclude_list: List[str]):
        result_list = []
        try:
            filenames = os.listdir(dirname)
            for filename in filenames:
                full_filename = os.path.join(dirname, filename)
                if os.path.isdir(full_filename):
                    result_list += cls.search_package(full_filename, exclude_list)
                else:
                    ext = os.path.splitext(full_filename)[-1]
                    if ext in (".py", ".pyc"):
                        if dirname not in result_list and filename not in exclude_list:
                            result_list.append(dirname)

        except PermissionError:
            pass

        return result_list

    @staticmethod
    def file_pointer(filename: StrPathLike, mode: str):
        return open(filename, mode, encoding="UTF-8", errors="ignore")

    @classmethod
    def move_dir(cls, src_dir: str, dst_dir: StrPathLike):
        # Python 3.9 이후부터 src_dir: StrPath 타입 가능. 아래 버전에는 `str`만 가능하다.
        # https://github.com/python/typeshed/blob/e88a182573ee0f6bf64ae1161977e4d05ccf25ba/stdlib/shutil.pyi#L107
        # https://bugs.python.org/issue32689
        if cls.is_exist(src_dir):
            shutil.move(src=src_dir, dst=dst_dir)


if __name__ == "__main__":
    pass
