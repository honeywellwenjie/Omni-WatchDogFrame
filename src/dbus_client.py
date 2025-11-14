import dbus


bus = dbus.SessionBus()
remote_object = bus.get_object('com.example.SampleService', '/com/example/SampleObject')
remote_interface = dbus.Interface(remote_object, 'com.example.SampleInterface')
response_a = remote_interface.method_a('Hello, Method A!')
print(response_a)
response_b = remote_interface.method_b('Hello, Method B!')
print(response_b)
response_c = remote_interface.method_c('Hello, Method C!')
print(response_c)

