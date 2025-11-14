#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from platform.fakeHardware_watchdog import FakeHardwareWatchdog

hwwatchdog = FakeHardwareWatchdog()

class hardware_watchdog:
    def __init__(self, path=None):
        hwwatchdog.__init__(path)

    def kick(self):
        return hwwatchdog.kick()

    def sett(self, timeout):
        return hwwatchdog.sett(timeout)

    def close(self):
        return hwwatchdog.close()

