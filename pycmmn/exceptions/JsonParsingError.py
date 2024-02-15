# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team, R&D Center.


class JsonParsingError(Exception):
    CODE = "[ERR0012]"

    def __str__(self):
        return self.CODE + " Json Parsing Error..."
