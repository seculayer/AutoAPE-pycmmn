# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team, R&D Center.


class DBConnectionError(Exception):
    CODE = "[ERR0002]"
    db_config = dict()

    def __init__(self, db_config):
        self.db_config = db_config

    def __str__(self):
        return self.CODE + " DB 접속정보 오류 발생.. "
