# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team, Intelligence R&D Center.


class ParameterError(Exception):
    CODE = "[ERR0008]"

    def __str__(self):
        return self.CODE + " Algorithm Parameter Invalid!"
