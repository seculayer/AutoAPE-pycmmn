# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.com
# Powered by Seculayer © 2021 Service Model Team, R&D Center.


class ETCException(Exception):
    ERROR_CODE = "[ERR0000]"

    def __str__(self):
        return self.ERROR_CODE + " 에러 발생.."
