# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team, R&D Center.


class NotSupportTypeError(Exception):
    CODE = "E0003"
    MSG = "[APEFlow {}]".format(CODE)
    TYPE = "None"

    def __init__(self, algorithm_type):
        self.TYPE = algorithm_type

    def __str__(self):
        return self.MSG + " this algorithm NOT SUPPORT {} type".format(self.TYPE)
