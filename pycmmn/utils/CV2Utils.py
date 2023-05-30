# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team
######################################################################################
import cv2
import numpy as np
from typing import Tuple


class CV2Utils(object):
    @staticmethod
    def imwrite(full_path: str, data: np.ndarray):
        cv2.imwrite(full_path, data)

    @staticmethod
    def resize(img, size: Tuple):
        return cv2.resize(img, size, interpolation=cv2.INTER_AREA)
