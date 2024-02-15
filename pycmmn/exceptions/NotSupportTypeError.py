# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team, R&D Center.


class NotSupportTypeError(Exception):
    CODE = "[ERR0007]"
    TYPE = "None"

    def __init__(self, data_type):
        self.TYPE = data_type

    def __str__(self):
        return self.CODE + " This Type({}) is NOT SUPPORTED".format(self.TYPE)
