#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import fcntl
import struct

class sf_watchdog:
    def __init__(self,path):
         self.devices = {}

    def register(self, name, timeout):
        self.devices[name] = timeout
        print("Device {} added successfully!".format(name))

    def start(self):

    def kick(self):
    
    def sett(self, name, timeout):

    def deregister(self, name):
        if name in self.devices:
            del self.devices[name]
            print("Device {} removed successfully!".format(name))
        else:
            print("Device {} not found!".format(name))

    def print_devices(self):
        if len(self.devices) == 0:
            print("No devices found!")
        else:
            print("Devices:")
            for name, timeout in self.devices.items():
                print("- {} (Time Parameter: {})".format(name, timeout))

    def close(self):

    

def sf_watchdog_test():


if __name__ == "__main__":
    software_watchdog_test()

