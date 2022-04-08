# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team, R&D Center.

import logging
import logging.config

from pycmmn.logger.MPLogHandler import MPLogHandler


class MPLogger(object):
    # Static variables
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

    def __init__(self, log_dir, log_name, log_level):
        # custom logger variables
        self.log_dir = log_dir
        self.log_name = log_name
        self.log_level = MPLogger._get_level(log_level)

        root = logging.getLogger()
        root.setLevel(self.log_level)

        logger = logging.getLogger(self.log_name)

        mpLogHandler = MPLogHandler("%s/%s.log" % (self.log_dir, self.log_name))
        mpLogHandler.setLevel(self.log_level)

        # Formatter
        formatter = logging.Formatter(
            "%(asctime)s %(levelname)-5s - %(processName)-15s - %(filename)-22s:%(lineno)-3s - %(message)s"
        )
        mpLogHandler.setFormatter(formatter)

        # Add handlers
        logger.addHandler(mpLogHandler)
        logger.propagate = False

        self.logger = logger

    def getLogger(self):
        # return logging.getLogger(self.log_name)
        return self.logger

    @staticmethod
    def _get_level(level):
        if level == "DEBUG":
            return logging.DEBUG
        elif level == "INFO":
            return logging.INFO
        elif level == "WARN":
            return logging.WARN
        elif level == "ERROR":
            return logging.ERROR
        elif level == "CRITICAL":
            return logging.CRITICAL
        else:  # 기본값
            return logging.INFO


if __name__ == '__main__':
    from multiprocessing import Process, Queue
    import time
    import tensorflow as tf
    tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.INFO)
    tf.compat.v1.Session()
    logger = MPLogger(log_dir="", log_name="test", log_level="INFO").getLogger()

    def worker_process(q):
        logger = logging.getLogger("test")
        idx = 0
        while True:
            try:
                logger.info("{} - test".format(idx))
                idx += 1
                if idx == 100:
                    idx = 0
                    raise NotImplementedError
            except Exception as e:
                logger.error(e, exc_info=True)
            time.sleep(0.1)
    q = Queue()
    workers = []
    for i in range(20):
        wp = Process(target=worker_process, name='worker %d' % (i + 1), args=(q,))
        workers.append(wp)
        wp.start()
    for wp in workers:
        wp.join()
