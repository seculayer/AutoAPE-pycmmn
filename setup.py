# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2021 AI Service Model Team, R&D Center.

# ----------------------------------------------------------------------------------------------
# AutoML - PYCMMN Setup Script
# ----------------------------------------------------------------------------------------------

from typing import List

from setuptools import setup, find_packages


class APEPythonSetup(object):
    def __init__(self):
        self.module_nm = "pycmmn"
        self.version = "1.0.0"

    @staticmethod
    def get_require_packages() -> List[str]:
        f = open("./requirements.txt", "r")
        require_packages = f.readlines()
        f.close()
        return require_packages

    @staticmethod
    def get_packages() -> List[str]:
        return find_packages(
            exclude=[
                "build", "tests", "scripts", "dists"
            ],
        )

    def setup(self) -> None:
        setup(
            name=self.module_nm,
            version=self.version,
            description="SecuLayer Inc. AutoML Project \n"
                        "Module : PYCMMN",
            author="Jin Kim",
            author_email="jin.kim@seculayer.com",
            packages=self.get_packages(),
            package_dir={},
            python_requires='>3.7',
            package_data={},
            install_requires=self.get_require_packages(),
            zip_safe=False,
        )


if __name__ == '__main__':
    print("    __  _____    ____  _____")
    print("   /  |/  / /   / __ \/ ___/")
    print("  / /|_/ / /   / /_/ /\__ \ ")
    print(" / /  / / /___/ ____/___/ / ")
    print("/_/  /_/_____/_/    /____/  ")
    print("                            ")
    APEPythonSetup().setup()
