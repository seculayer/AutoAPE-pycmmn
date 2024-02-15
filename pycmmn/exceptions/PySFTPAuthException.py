# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2020 AI Service Model Team, R&D Center.


class PySFTPAuthException(Exception):
    CODE = "[ERR0009]"

    def __init__(self, con_info_dict: dict):
        self.info_dict = con_info_dict

    def __str__(self):
        return f"{self.CODE} Authentication failed. check username and password! {self.info_dict}"
