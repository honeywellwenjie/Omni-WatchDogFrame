import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GObject


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

DBusGMainLoop(set_as_default=True)
loop = GObject.MainLoop()
watchdog_dbus()
loop.run()

