# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.com
# Powered by Seculayer © 2021 Service Model Team, R&D Center.


class VersionManagementError(Exception):
    CODE = "[ERR0011]"

    def __init__(self):
        Exception.__init__(self)

    def __str__(self) -> str:
        return self.CODE + " {}".format(type(self).__name__)


if __name__ == '__main__':
    try:
        raise VersionManagementError()
    except VersionManagementError as e:
        print(str(e))
