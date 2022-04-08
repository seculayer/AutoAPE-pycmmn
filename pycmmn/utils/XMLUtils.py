# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team

######################################################################################

from xml.etree.ElementTree import ElementTree, parse, fromstring


class XMLUtils(object):
    @staticmethod
    def xml_load(**kwargs):
        xml_file_name = kwargs["filename"]
        tree = parse(xml_file_name)

        return tree

    @staticmethod
    def xml_load_str(xml_str):
        tree = ElementTree(fromstring(xml_str))
        return tree

    @staticmethod
    def xml_write(**kwargs):
        xml_file_name = kwargs["filename"]
        # indent

        ElementTree(kwargs["element"]).write(
            xml_file_name, encoding="utf-8", xml_declaration=True
        )

    @staticmethod
    def xml_parse(root, _key):
        if root is None:
            return None
        else:
            root_keys = root.findall(_key)
            return root_keys

    @staticmethod
    def indent(elem, level=0):
        i = "\n" + level * "\t"
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "\t"
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                XMLUtils.indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i
        return elem

    @classmethod
    def xml2dict_list(cls, xml_data, keys):
        res_dict_list = list()
        for data in xml_data:
            res_dict_list.append(cls._xml2dict(xml_data=data, keys=keys))

        return res_dict_list

    @staticmethod
    def _xml2dict(xml_data, keys):
        res_dict = dict()
        for key in keys:
            try:
                res_dict[key] = xml_data.attrib[key]
            except :
                res_dict[key] = None
        return res_dict

    @staticmethod
    def find(xml_data, key):
        return xml_data.find(key).text


if __name__ == '__main__':
    XMLUtils.xml_load(filename="./example.xml")