#!/usr/bin/python3
"""
This script is intended to retrieve the currently existing running configuration from Arista EOS devices.
Tested against Arista vEOS-Lab images
"""
import pyeapi

NODE = pyeapi.connect_to('Spine-1')
IP = pyeapi.config_for('Spine-1')['host']

output = NODE.get_config('running-config')
cfg = '\n'.join(output)

with open(f'{IP}-config.txt', '+w') as file:
    file.write(cfg)




