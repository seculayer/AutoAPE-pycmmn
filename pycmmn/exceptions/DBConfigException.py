# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team, R&D Center.


class DBConfigException(Exception):
    CODE = "E0002"
    MSG = "[pycmmn {}]".format(CODE)
    db_config = dict()

    def __init__(self, db_config):
        self.db_config = db_config

    def __str__(self):
        return self.MSG + " DB Config dictionary : {}".format(self.db_config)
