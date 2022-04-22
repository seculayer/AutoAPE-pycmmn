# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team, R&D Center.


class GPUMemoryError(Exception):
    CODE = "E0041"
    MSG = "[APEFlow {}]".format(CODE)

    def __str__(self):
        return self.MSG + "GPU Memory Error"
