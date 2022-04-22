# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team
######################################################################################

import os
import shutil


class FileUtils(object):
    @staticmethod
    def read_dir(directory="./", ext=".done"):
        file_names = os.listdir(directory)

        res_file_names = list()
        for file_name in file_names:
            if ext == os.path.splitext(file_name)[-1]:
                res_file_names.append("%s/%s" % (directory, file_name))

        return res_file_names

    @staticmethod
    def mkdir(dir_name):
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

    @staticmethod
    def get_realpath(file=None):
        return os.path.dirname(os.path.realpath(file))

    @classmethod
    def remove_dir(cls, dir_name):
        if cls.is_exist(dir_name):
            shutil.rmtree(dir_name)

    @staticmethod
    def is_exist(file):
        return os.path.exists(file)

    @classmethod
    def search_package(cls, dirname, exclude_list):
        result_list = list()
        try:
            filenames = os.listdir(dirname)
            for filename in filenames:
                full_filename = os.path.join(dirname, filename)
                if os.path.isdir(full_filename):
                    result_list += cls.search_package(full_filename, exclude_list)
                else:
                    ext = os.path.splitext(full_filename)[-1]
                    if ext == '.py' or ext == ".pyc":
                        if dirname not in result_list and filename not in exclude_list:
                            result_list.append(dirname)

        except PermissionError:
            pass

        return result_list

    @staticmethod
    def file_pointer(filename, mode):
        return open(filename, mode, encoding='UTF-8', errors='ignore')

    @classmethod
    def move_dir(cls, src_dir, dst_dir):
        if cls.is_exist(src_dir):
            shutil.move(src=src_dir, dst=dst_dir)


if __name__ == '__main__':
    pass
