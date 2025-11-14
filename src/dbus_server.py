#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib

from logger import logger

class watchdog_dbus(dbus.service.Object):
    def __init__(self):
        bus_name = dbus.service.BusName('com.example.watchdogService', bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/com/example/watchdogObject')

    @dbus.service.method('com.example.watchdog', in_signature='s', out_signature='s')
    def watchdog_dbus_add(self, message):
        print('watchdog_dbus_add: %s' % message)
        return 'watchdog_dbus_add: Received: %s' % message

    @dbus.service.method('com.example.watchdog', in_signature='s', out_signature='s')
    def watchdog_dbus_del(self, message):
        print('watchdog_dbus_del: %s' % message)
        return 'watchdog_dbus_del Received: %s' % message

    @dbus.service.method('com.example.watchdog', in_signature='s', out_signature='s')
    def watchdog_dbus_kick(self, message):
        print('watchdog_dbus_kick: %s' % message)
        return 'watchdog_dbus_kick Received: %s' % message

    @dbus.service.method('com.example.watchdog', in_signature='s', out_signature='s')
    def watchdog_dbus_settime(self, message):
        print('watchdog_dbus_settime: %s' % message)
        return 'watchdog_dbus_settime Received: %s' % message


def soft_watchdog_main():
    logger.info("Starting soft-watchdog daemon ...")

    DBusGMainLoop(set_as_default=True)
    mainloop = GLib.MainLoop()
    watchdog_dbus()
    mainloop.run()
    print('dbus main loop running ...')

if __name__ == "__main__":
    soft_watchdog_main()