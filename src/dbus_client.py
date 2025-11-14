import dbus


bus = dbus.SessionBus()
remote_object = bus.get_object('com.example.SampleService', '/com/example/SampleObject')
remote_interface = dbus.Interface(remote_object, 'com.example.SampleInterface')
response = remote_interface.sample_method('Hello, DBus!')
print(response)

