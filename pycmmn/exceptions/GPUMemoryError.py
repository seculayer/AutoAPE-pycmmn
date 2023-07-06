# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team, R&D Center.


class GPUMemoryError(Exception):
    CODE = "[ERR006]"

    def __str__(self):
        return self.CODE + " GPU Out of Memory Error"
