# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team, Intelligence R&D Center.


class ParameterError(Exception):
    CODE = "E0001"
    MSG = "[APEFlow {}]".format(CODE)

    def __str__(self):
        return self.MSG + " algorithm parameter invalid!"
