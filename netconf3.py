from ietf_ip_binding import ietf_interfaces
model = ietf_interfaces()
#print(model.get())

new_interface = model.interfaces.interface.add('GigabitEthernet2')
print(new_interface.get())
