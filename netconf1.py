from ncclient import manager
import xml.etree.ElementTree as ET

m = manager.connect(host='sandbox-iosxe-latest-1.cisco.com',
                    port=830,
                    username='admin',
                    password='C1sco12345',
                    device_params={'name': 'csr'})

#for capability in m.server_capabilities:
#    print(capability)

schema = m.get_schema('ietf-ip')
#print(schema)

root = ET.fromstring(schema.xml)
yang_text = list(root)[0].text
with open ('ietf-ip.yang','w') as f:
    f.write(yang_text)
