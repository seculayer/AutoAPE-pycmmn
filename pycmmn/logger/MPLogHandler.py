# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2021 Service Model Team, R&D Center.
import sys
import logging
import traceback
import threading
import multiprocessing
from logging import FileHandler as FH
from logging import StreamHandler as SH


# ============================================================================
# Define Log Handler
# ============================================================================
class MPLogHandler(logging.Handler):
    """multiprocessing log handler

    This handler makes it possible for several processes
    to log to the same file by using a queue.

    """
    def __init__(self, fname):
        logging.Handler.__init__(self)

        self._f_handler = FH(fname)
        self._f_handler.suffix = '%Y-%m-%d'
        self._s_handler = SH()
        self.queue = multiprocessing.Queue(-1)

        thrd = threading.Thread(target=self.receive)
        thrd.daemon = True
        thrd.start()

    def setFormatter(self, fmt):
        logging.Handler.setFormatter(self, fmt)
        self._f_handler.setFormatter(fmt)
        self._s_handler.setFormatter(fmt)

    def receive(self):
        while True:
            try:
                record = self.queue.get()
                self._f_handler.emit(record)
                self._s_handler.emit(record)
            except (KeyboardInterrupt, SystemExit):
                raise
            except EOFError:
                break
            except:
                traceback.print_exc(file=sys.stderr)

    def send(self, s):
        self.queue.put_nowait(s)

    def _format_record(self, record):
        if record.args:
            record.msg = record.msg % record.args
            record.args = None
        if record.exc_info:
            dummy = self.format(record)
            record.exc_info = None

        return record

    def emit(self, record):
        try:
            s = self._format_record(record)
            self.send(s)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

    def setLevel(self, level):
        logging.Handler.setLevel(self, level)
        self._f_handler.setLevel(level)
        self._s_handler.setLevel(level)

    def close(self):
        self._f_handler.close()
        self._s_handler.close()
        logging.Handler.close(self)
