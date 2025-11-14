#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import threading

from logger import logger
from soft_watchdog import softwatchdog_dbus_thread, monitor_softwatchdog_thread
from hard_watchdog import hardware_watchdog


def monitor_threads(*threads):
    for t in threads:
        if not t.is_alive():
            logger.error(f"Thread {t.name} is dead!")
            return False
    return True


def main():
    log = logger
    log.info("Omni-watchdog daemon booting")

    hwd = hardware_watchdog()
    hwd.sett(30)
    time.sleep(0.3)

    dbus_thread = threading.Thread(target=softwatchdog_dbus_thread, name="dbus-thread")
    soft_thread = threading.Thread(target=monitor_softwatchdog_thread, name="softwd-thread")

    dbus_thread.start()
    soft_thread.start()

    time.sleep(1)

    while True:
        if not hwd.kick():
            break

        if not monitor_threads(dbus_thread, soft_thread):
            os.system("sudo reboot &")
            break

        time.sleep(5)

    hwd.close()


if __name__ == "__main__":
    main()
