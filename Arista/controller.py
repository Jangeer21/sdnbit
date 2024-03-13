#!/usr/bin/env python3

"""
Arista EOS network automation with pyeapi.
"""

import pyeapi

SPINE1 = pyeapi.connect_to('Spine-1')
SPINE2 = pyeapi.connect_to('Spine-2')
LEAF1 = pyeapi.connect_to('Leaf-1')
LEAF2 = pyeapi.connect_to('Leaf-2')
LEAF3 = pyeapi.connect_to('Leaf-3')
LEAF4 = pyeapi.connect_to('Leaf-4')

print(SPINE1.api)

NODES = [SPINE1, SPINE2, LEAF1, LEAF2, LEAF3, LEAF4]

for NODE in NODES:
    try:
        output = NODE.enable('show version')
        print('SN -> ', output[0]['result']['serialNumber'])
    except (TimeoutError, pyeapi.eapilib.ConnectionError):
        print('Device unavailable')

