# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.com
# Powered by Seculayer © 2021 Service Model Team, R&D Center.


class FileLoadError(Exception):
    ERROR_CODE = "[ERR0001]"

    def __init__(self, file_name):
        self.file_name = file_name

    def __str__(self):
        return self.ERROR_CODE + " 파일을 찾을 수 없습니다...[{}]".format(self.file_name)
