# start by importing the library
import pyeapi

# create a node object by specifying the node to work with
node = pyeapi.connect_to('Spine-1')
output = node.enable('show version')
print(output)
# send one or more commands to the node
#node.enable('show hostname')

# return the running or startup configuration from the
# node (output omitted for brevity)
#node.running_config

vlans = node.api('vlans')
print(vlans.getall())