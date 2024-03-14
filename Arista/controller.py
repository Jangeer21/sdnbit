#!/usr/bin/python3
"""
Arista EOS network automation with pyeapi.
"""

import pyeapi
from pprint import pprint

NODE = pyeapi.connect_to('Spine-1')

output = NODE.enable('show version')
pprint(output)


#NODE = pyeapi.connect(host='192.168.1.5',username='arista',password='arista')

#output = NODE.enable('show running-config')
#output = NODE.run_commands('show running-config')
#output = NODE.startup_config
#output = NODE.execute(['enable','show running-config'])