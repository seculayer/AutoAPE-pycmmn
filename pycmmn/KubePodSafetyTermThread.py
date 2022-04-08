# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2021 Service Model Team, R&D Center. 

# ---- python base packages
import threading
import signal


class KubePodSafetyTermThread(threading.Thread):
    # class : KubePodSafetyTermThread
    def __init__(self):
        threading.Thread.__init__(self)

        # Thread terminate
        self.__exit = False
        signal.signal(signal.SIGINT, self._sigterm_handler)
        signal.signal(signal.SIGTERM, self._sigterm_handler)

    def _sigterm_handler(self, _signo, _stack_frame):
        self.__exit = True

    def _is_exit(self):
        return self.__exit
