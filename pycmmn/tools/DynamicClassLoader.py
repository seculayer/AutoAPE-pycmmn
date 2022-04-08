# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team, R&D Center.
import importlib

from pycmmn.utils.FileUtils import FileUtils
from pycmmn.exceptions.DynamicClassModuleNotExist import DynamicClassModuleNotExist


class DynamicClassLoader(object):

    @staticmethod
    def load_module(package, class_nm):
        # return loaded Class
        return getattr(importlib.import_module(package + "." + class_nm), class_nm)

    @classmethod
    def load_multi_packages(cls, packages, class_nm, logger):
        for package in packages:
            try:
                return cls.load_module(package, class_nm)

            except (ModuleNotFoundError, FileNotFoundError):
                continue

            except Exception as e:
                logger.error(e, exc_info=True)

        raise DynamicClassModuleNotExist(class_nm)

    @classmethod
    def get_packages(cls, target_dir, exclude_files, lib_path):
        path_packages = list(set(FileUtils.search_package(target_dir, exclude_files)))
        results = list()
        for package in path_packages:
            results.append(cls.cvt_package(lib_path, package))
        return results

    @classmethod
    def cvt_package(cls, target_dir, package):
        return package.replace(target_dir, '').replace("/", ".")


if __name__ == '__main__':
    from pycmmn.logger.MPLogger import MPLogger
    try:
        print(DynamicClassLoader.load_multi_packages(
            ["pycmmn.common", "pycmmn.db"], "DBFactory", MPLogger("./", "temp", "INFO").getLogger())
        )
    except Exception as err:
        print(str(err))

    print(
        DynamicClassLoader.get_packages(
            target_dir=FileUtils.get_realpath(__file__) + "/../../",
            exclude_files=["__init__.py"],
            lib_path=FileUtils.get_realpath(__file__) + "/../../"
        )
    )

    print(DynamicClassLoader.load_multi_packages(
        ["pycmmn.common", "algorithms"], "Test", MPLogger("./", "temp", "INFO").getLogger())().MSG
    )
