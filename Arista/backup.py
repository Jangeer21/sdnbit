#!/usr/bin/python3
"""
This script is intended to retrieve the currently existing running configuration from Arista EOS devices.
Tested against Arista vEOS-Lab images.
"""
import pyeapi

NODES = ['Spine-1','Spine-2','Leaf-1','Leaf-2','Leaf-3','Leaf-4']

for NODE in NODES:
    try:
        INSTANCE = pyeapi.connect_to(NODE)
        IP = pyeapi.config_for(NODE)['host']
        output = INSTANCE.get_config('running-config')
        cfg = '\n'.join(output)

        with open(f'{IP}-config.txt', '+w') as file:
            file.write(cfg)

    except ConnectionError:
        print('Failed to retrieve configuration from ', IP)
        pass
