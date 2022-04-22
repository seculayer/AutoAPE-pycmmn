# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team, R&D Center.

from __future__ import print_function

import sys
import re
import datetime
import os

from pycmmn.exceptions.VersionManagementError import VersionManagementError


class VersionManagement(object):
    def __init__(self, app_path=None):
        try:
            if app_path is None:
                app_path = os.getcwd()

            _VER_INFO = self._get_version(app_path)
            self.MODULE_NM = _VER_INFO.get("module", "pycmmn")
            self.VERSION = _VER_INFO.get("version", "1.0.0")
            self.BUILD_DATE = _VER_INFO.get("build date", "999912312359")
            self.REVISION = _VER_INFO.get("revision", "1")

        except VersionManagementError:
            raise VersionManagementError

    def print_version(self):
        ver_str = "\n-------------------------------------------------------------------------------\n"
        ver_str += "eyeCloudAI - Python Module ({})\n".format(self.MODULE_NM)
        ver_str += "  - version : {}\n".format(self.VERSION)
        ver_str += "  - build date : {}\n".format(self.BUILD_DATE)
        ver_str += "  - revision : {}\n".format(self.REVISION)
        ver_str += "-------------------------------------------------------------------------------"
        return ver_str

    @staticmethod
    def _get_version(app_path):
        f = None
        try:
            if app_path is None:
                app_path = os.getcwd()

            results = dict()
            p = re.compile("(.+) : (.+)")
            f = open(app_path + "/VERSION", "r")
            for line in f.readlines():
                parsed = p.match(line).groups()
                results[parsed[0]] = parsed[1]

        except Exception:
            raise VersionManagementError()
        finally:
            if f is not None:
                f.close()

        return results

    @staticmethod
    def generate(version="1.0.0", app_path=None, module_nm="mlps"):
        if app_path is None:
            app_path = os.getcwd()

        filename = app_path + "/VERSION"
        try:
            f = open(filename, "w")
            f.write(
                "module : {}\n"
                "version : {}\n"
                "build date : {}\n"
                "revision : {}\n".format(
                    module_nm, version, datetime.datetime.now().strftime("%Y%m%d%H%M"), 1
                )
            )
        except Exception:
            raise VersionManagementError()
        print("version information file created...[{}]".format(filename))


if __name__ == '__main__':
    try:
        if sys.argv[1] == "version" or sys.argv[1] == "-v":
            print(VersionManagement().print_version())
        elif sys.argv[1] == "revision" or sys.argv[1] == "-r":
            if len(sys.argv) == 3:
                path = sys.argv[2]
                print(VersionManagement(app_path=path).REVISION)
            else:
                print(VersionManagement().REVISION)

    except IndexError as e:
        print("usage : {} [version|-v|build|-b|revision|-r] [VERSION] [PATH] [MODULE NAME]".format(sys.argv[0]))
