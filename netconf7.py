from ncclient import manager
import xml.etree.ElementTree as ET

m = manager.connect(host='sandbox-iosxe-latest-1.cisco.com',
                    port=830,
                    username='admin',
                    password='C1sco12345',
                    device_params={'name': 'csr'})

with open('interface.xml') as f:
    xml =f.read()
reply = m.edit_config(config=xml,target='running')
print(reply)
m.close_session()
