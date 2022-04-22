# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team
######################################################################################

from pycmmn.utils.XMLUtils import XMLUtils


# XML Configuration file handling
class ConfUtils(object):
    @staticmethod
    def load(**kwargs) -> dict:
        conf_xml_filename = kwargs["filename"]

        configuration = XMLUtils.xml_load(filename=conf_xml_filename)

        conf_dict = dict()

        for _property in configuration.findall("property"):
            conf_dict[_property.find("name").text] = _property.find("value").text

        return conf_dict
