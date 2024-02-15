# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team, R&D Center.


class ValidationError(Exception):
    CODE = "[ERR0010]"

    def __str__(self):
        return self.CODE + "ML Algorithm Validation ERROR!"
