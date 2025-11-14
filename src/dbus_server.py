import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GObject


class Example(dbus.service.Object):
    def __init__(self):
        bus_name = dbus.service.BusName('com.example.SampleService', bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/com/example/SampleObject')

    @dbus.service.method('com.example.SampleInterface', in_signature='s', out_signature='s')
    def sample_method(self, message):
        print('Received message: %s' % message)
        return 'Received: %s' % message


DBusGMainLoop(set_as_default=True)
loop = GObject.MainLoop()
Example()
loop.run()

