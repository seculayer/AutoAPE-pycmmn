# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team, R&D Center.


class DynamicClassModuleNotExist(Exception):
    CODE = "[ERR0003]"

    def __init__(self, class_nm):
        Exception.__init__(self)
        self.class_nm = class_nm

    def __str__(self):
        return self.CODE + " Class를 찾을 수 없습니다... {}.py 또는 {}.pyc 파일을 확인하세요!".format(self.class_nm, self.class_nm)
