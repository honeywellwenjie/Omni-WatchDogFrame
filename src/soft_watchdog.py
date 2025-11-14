#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib

from logger import logger

soft_watchdog_list = []

class sfwatchdog_dbus(dbus.service.Object):
    INTERFACE = 'com.example.SFwatchdog'
    OBJECT_PATH = '/com/example/SFwatchdogObject'
    BUS_NAME = 'com.example.SFwatchdogService'

    def __init__(self):
        self.log = logger
        self.sf_wthdog = soft_watchdog()

        bus = dbus.SessionBus()
        bus_name = dbus.service.BusName(self.BUS_NAME, bus=bus)
        dbus.service.Object.__init__(self, bus_name, self.OBJECT_PATH)

        self.log.info("  |-- watchdog dbus bootup ... (session bus)")

    @dbus.service.method(INTERFACE, in_signature='s', out_signature='s')
    def sfwatchdog_dbus_add(self, message):
        self.log.info('sfwatchdog_dbus_add: %s' % message)
        self.sf_wthdog.add_soft_watchdog(message)
        return 'add_soft_watchdog : %s' % message

    @dbus.service.method(INTERFACE, in_signature='s', out_signature='s')
    def sfwatchdog_dbus_del(self, message):
        self.log.info('sfwatchdog_dbus_del: %s' % message)
        ok = self.sf_wthdog.remove_soft_watchdog(message)
        if ok:
            return 'remove_soft_watchdog : %s' % message
        else:
            return 'remove_soft_watchdog : %s fail (not exist)' % message

    @dbus.service.method(INTERFACE, in_signature='s', out_signature='s')
    def sfwatchdog_dbus_kick(self, message):
        self.log.debug('sfwatchdog_dbus_kick: %s' % message)
        ok = self.sf_wthdog.kick_soft_watchdog(message)
        if ok:
            return 'kick_soft_watchdog : %s' % message
        else:
            return 'kick_soft_watchdog : %s fail (not exist)' % message

    @dbus.service.method(INTERFACE, in_signature='s', out_signature='s')
    def sfwatchdog_dbus_settime(self, message):
        self.log.info('sfwatchdog_dbus_settime: %s' % message)
        elements = message.split(":")

        if len(elements) != 2:
            self.log.error('sett format wrong: %s. Example: watchdog:30' % message)
            return 'sett_soft_watchdog : %s fail' % message

        name = elements[0].strip()
        time_str = elements[1].strip()

        if not time_str.isdigit():
            self.log.error('sett format wrong: %s time is not digit' % message)
            return 'sett_soft_watchdog : %s fail' % message

        timeout = int(time_str)
        ok = self.sf_wthdog.sett_soft_watchdog(name, timeout)

        if ok:
            self.log.info("sett_soft_watchdog %s : %d" % (name, timeout))
            return 'sett_soft_watchdog %s success' % message
        else:
            self.log.error("sett_soft_watchdog failed watchdog not registered yet : %s" % message)
            return 'sett_soft_watchdog failed watchdog not registered yet : %s' % message


class soft_watchdog:
    def __init__(self):
        self.log = logger
        self.lock = threading.Lock()
        self.list = soft_watchdog_list

    def add_soft_watchdog(self, name):
        with self.lock:
            existing = None
            for obj in self.list:
                if obj['name'] == name:
                    existing = obj
                    break

            if existing is not None:
                self.log.info("soft watchdog %s already exist. remove it ..." % name)
                self.list.remove(existing)
                self.log.info("remove_soft_watchdog %s" % name)

            sf_wthdog_obj = {
                'name': name,
                'started': False,
                'timeout': 60,
                'current_time': 0,
            }
            self.list.append(sf_wthdog_obj)
            self.log.info("add_soft_watchdog %s" % name)

    def remove_soft_watchdog(self, name):
        with self.lock:
            for obj in self.list:
                if obj['name'] == name:
                    self.list.remove(obj)
                    self.log.info("remove_soft_watchdog %s" % name)
                    return True

            self.log.error("soft_watchdog %s not exist" % name)
            return False

    def kick_soft_watchdog(self, name):
        with self.lock:
            for obj in self.list:
                if obj['name'] == name:
                    obj['started'] = True
                    obj['current_time'] = 0
                    self.log.info("kick_soft_watchdog %s" % name)
                    return True

            self.log.error("soft_watchdog %s not exist" % name)
            return False

    def sett_soft_watchdog(self, name, timeout):
        with self.lock:
            for obj in self.list:
                if obj['name'] == name:
                    obj['started'] = False
                    obj['current_time'] = 0
                    obj['timeout'] = timeout
                    self.log.info("sett_soft_watchdog %s : %d" % (name, timeout))
                    return True

            self.log.error("soft_watchdog %s not exist" % name)
            return False


def soft_watchdog_main():
    logger.info("Starting soft-watchdog daemon ...")

    DBusGMainLoop(set_as_default=True)
    sfwatchdog_dbus()

    logger.info("DBus main loop starting ...")
    mainloop = GLib.MainLoop()
    mainloop.run()

    logger.info("DBus main loop exited")


if __name__ == "__main__":
    soft_watchdog_main()
