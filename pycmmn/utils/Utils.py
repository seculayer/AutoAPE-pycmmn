#  -*- coding: utf-8 -*-
#  Author : Manki Baek
#  e-mail : manki.baek@seculayer.com
#  Powered by Seculayer © 2021 Service Model Team, R&D Center.
#
import datetime
import threading
import time

from pycmmn.Singleton import Singleton


class Utils(object, metaclass=Singleton):

    @staticmethod
    def make_timer(logger, max_time=5):
        return Timer(logger, max_time=max_time)

    @staticmethod
    def get_current_time():
        return datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    @staticmethod
    def get_current_time_without_sec():
        return datetime.datetime.now().strftime("%Y%m%d%H%M")

    @staticmethod
    def get_current_time_with_mili_sec():
        return datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")


class Timer(threading.Thread):
    def __init__(self, logger, max_time=5):
        threading.Thread.__init__(self)

        self.logger = logger
        self._suspend = False
        self._exit = False

        self.MAX_TIME = max_time
        self.CURRENT_TIME = 0
        self.SAVE_TIME = 0

    def run(self):
        while self._exit is False:
            self.CURRENT_TIME = time.time()
            time.sleep(0.5)

    def set_time(self):
        self.SAVE_TIME = time.time()

    def timeout(self):
        if self.CURRENT_TIME - self.SAVE_TIME > self.MAX_TIME:
            # self.mlps_logger.info("timer exit")
            return True
        else:
            return False

    def suspend(self):
        self._suspend = True

    def resume(self):
        self._suspend = False

    def exit(self):
        self._exit = True
