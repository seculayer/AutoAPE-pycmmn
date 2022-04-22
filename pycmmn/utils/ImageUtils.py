# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2021 AI Service Model Team, R&D Center.
import cv2
import numpy as np


class ImageUtils(object):
    def __init__(self):
        pass

    @staticmethod
    def load(buffer) -> np.array:
        img_array = np.frombuffer(buffer, dtype=np.uint8)
        return cv2.imdecode(img_array, cv2.IMREAD_COLOR)
