#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import fcntl
import struct

from logger import logger

WDIOC_GETTIMEOUT = 0x80045707
WDIOC_SETTIMEOUT = 0xc0045706
WATCHDOG_DEV = "/dev/watchdog0"
class LinuxHardwareWatchdog:
    def __init__(self, path=None):
        self.log = logger
        self.dev = path if path is not None else WATCHDOG_DEV
        try:
            self.fd = os.open(self.dev, os.O_WRONLY)
            self.log.info("Jetson HW watchdog device opened successfully: %s" % self.dev)
        except Exception as e:
            self.log.error("Failed to open Jetson watchdog device: %s" % str(e))
            self.fd = None

    def kick(self):
        if self.fd is None:
            self.log.error("Jetson HW watchdog not opened")
            return False
        try:
            os.write(self.fd, b'\0')
            self.log.debug("Jetson watchdog kicked")
            return True
        except Exception as e:
            self.log.error("Failed to kick Jetson watchdog: %s" % str(e))
            return False

    def sett(self, timeout):
        if self.fd is None:
            self.log.error("Jetson HW watchdog not opened")
            return False
        try:
            fcntl.ioctl(self.fd, WDIOC_SETTIMEOUT, struct.pack('L', timeout), True)
            self.log.info("Jetson watchdog timeout set to %d" % timeout)
            return True
        except Exception as e:
            self.log.error("Failed to set Jetson watchdog timeout: %s" % str(e))
            return False

    def close(self):
        if self.fd is None:
            return True
        try:
            os.close(self.fd)
            self.log.info("Jetson watchdog device closed")
        except Exception as e:
            self.log.error("Failed to close Jetson watchdog: %s" % str(e))
        self.fd = None
        return True

class FakeHardwareWatchdog:
    def __init__(self, path=None):
        print("[FAKE] init fake watchdog")

    def kick(self):
        print("[FAKE] kick fake watchdog")
        return True

    def sett(self, timeout):
        print(f"[FAKE] set fake timeout {timeout}")
        return True

    def close(self):
        print("[FAKE] close fake watchdog")
        return True

