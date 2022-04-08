# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2020 AI Service Model Team, R&D Center.


class PySFTPAuthException(Exception):
    def __str__(self):
        return "[ERROR-C0001] Authentication failed. check username and password!"
