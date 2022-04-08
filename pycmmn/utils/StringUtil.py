# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.com
# Powered by Seculayer © 2021 Service Model Team, R&D Center.


class StringUtil(object):

    @staticmethod
    def get_int(data) -> int:
        try:
            return int(data)
        except ValueError:
            return -1

    @staticmethod
    def get_boolean(data) -> bool:
        val = str(data).lower()
        if val == "y" or val == "true":
            return True
        else:
            return False
