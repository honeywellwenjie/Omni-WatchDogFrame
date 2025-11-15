#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from linux_hwtd import FakeHardwareWatchdog
#from linux_hwtd import LinuxHardwareWatchdog

hwwatchdog = None
class hardware_watchdog:
    def __init__(self, path=None):
        global hwwatchdog
        if hwwatchdog is None:
            hwwatchdog = FakeHardwareWatchdog(path)
            #hwwatchdog = LinuxHardwareWatchdog(path)

    def kick(self):
        return hwwatchdog.kick()

    def sett(self, timeout):
        return hwwatchdog.sett(timeout)

    def close(self):
        return hwwatchdog.close()