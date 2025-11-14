import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GObject


class test(dbus.service.Object):
    def __init__(self):
        bus_name = dbus.service.BusName('com.example.SampleService', bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/com/example/SampleObject')

    @dbus.service.method('com.example.SampleInterface', in_signature='s', out_signature='s')
    def method_a(self, message):
        print('Received message in Method A: %s' % message)
        return 'Method A Received: %s' % message

    @dbus.service.method('com.example.SampleInterface', in_signature='s', out_signature='s')
    def method_b(self, message):
        print('Received message in Method B: %s' % message)
        return 'Method B Received: %s' % message

    @dbus.service.method('com.example.SampleInterface', in_signature='s', out_signature='s')
    def method_c(self, message):
        print('Received message in Method C: %s' % message)
        return 'Method C Received: %s' % message


DBusGMainLoop(set_as_default=True)
loop = GObject.MainLoop()
test()
loop.run()

