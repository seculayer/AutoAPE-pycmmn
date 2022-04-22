# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.com
# Powered by Seculayer © 2021 Service Model Team, R&D Center.


class JobFileLoadError(Exception):
    ERROR_CODE = "[MLPS0001]"

    def __init__(self, key):
        self.key = key

    def __str__(self):
        return self.ERROR_CODE + " Job File Load Error... Check {}".format(self.key)
