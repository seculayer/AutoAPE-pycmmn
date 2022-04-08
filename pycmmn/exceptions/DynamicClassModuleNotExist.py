# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team, R&D Center.


class DynamicClassModuleNotExist(Exception):
    CODE = "E0001"
    MSG = "[pycmmn {}]".format(CODE)

    def __init__(self, class_nm):
        Exception.__init__(self)
        self.class_nm = class_nm

    def __str__(self):
        return self.MSG + " Class file Not Found ... Check {}.py or {}.pyc file!".format(self.class_nm, self.class_nm)
