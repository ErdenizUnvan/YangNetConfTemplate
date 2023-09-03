from ietf_ip_binding import ietf_interfaces
import pyangbind.lib.pybindJSON as pybindJSON
import json

model = ietf_interfaces()
#print(model.get())

new_interface = model.interfaces.interface.add('GigabitEthernet2')
new_interface.description = 'NETCONF-CONFIGURED PORT'
ipv4_addr = new_interface.ipv4.address.add('12.12.12.2')
ipv4_addr.netmask = '255.255.255.0'

json_data = pybindJSON.dumps(model, mode='ietf')

with open('new_interface.json','w') as f:
    f.write(json_data)

print(json_data)
