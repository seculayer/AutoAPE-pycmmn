#  -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.com
#  Powered by Seculayer © 2021 Service Model Team, R&D Center.
#

import json

from pycmmn.Singleton import Singleton
from pycmmn.Constants import Constants


class Common(object, metaclass=Singleton):
    with open(Constants.DIR_RESOURCES + "/rest_url_info.json", "r") as f:
        REST_URL_DICT = json.load(f)
