from ietf_ip_binding import ietf_interfaces
model = ietf_interfaces()
#print(model.get())

new_interface = model.interfaces.interface.add('GigabitEthernet2')
#print(new_interface.get())

new_interface.description = 'NETCONF-CONFIGURED PORT'
#print(new_interface.get()['description'])

ipv4_addr = new_interface.ipv4.address.add('12.12.12.2')
#print(ipv4_addr.get())
ipv4_addr.netmask = '255.255.255.0'
print(ipv4_addr.get())
