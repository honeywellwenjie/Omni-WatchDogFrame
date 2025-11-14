import dbus

bus = dbus.SessionBus()
remote_object = bus.get_object('com.example.watchdogService', '/com/example/watchdogObject')
remote_interface = dbus.Interface(remote_object, 'com.example.watchdog')
response_a = remote_interface.watchdog_dbus_add('Hello, Method A!')
print(response_a)
response_b = remote_interface.watchdog_dbus_kick('Hello, Method B!')
print(response_b)
response_c = remote_interface.watchdog_dbus_settime('Hello, Method C!')
print(response_c)

