#  -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.com
#  Powered by Seculayer © 2021 Service Model Team, R&D Center.

from pycmmn.Singleton import Singleton
from pycmmn.utils.FileUtils import FileUtils


class Constants(object, metaclass=Singleton):
    DIR_RESOURCES = FileUtils.get_realpath(file=__file__) + "/resources"

    JOB_TYPE_LEARN = "learn"
    JOB_TYPE_INFERENCE = "inference"

    DATASET_FORMAT_TEXT = "1"
    DATASET_FORMAT_IMAGE = "2"
