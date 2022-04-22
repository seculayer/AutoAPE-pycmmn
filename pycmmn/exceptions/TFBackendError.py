# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team, R&D Center.


class TFBackendError(Exception):
    CODE = "E0002"
    MSG = "[APEFlow {}]".format(CODE)

    def __str__(self):
        return self.MSG + " ALGORITHM VERSION 이 맞지 않습니다. Multi 알고리즘의 TensorFlow 버전을 확인해 주세요."
