#!/usr/bin/env python
import pyeapi

def retrieve_running_config(device_name):
    try:
        # Connect to the EOS device using the device name
        node = pyeapi.connect_to(device_name)

        # Send the "show running-config" command
        response = node.enable('show running-config')

        # Extract and print the running configuration
        running_config = response[0]['result']['output']
        print(running_config)
        #print(f"Running config for {device_name}:\n{running_config}\n{'=' * 40}")
    except AttributeError as e:
        print(f"Error occurred while retrieving running config for {device_name}: {e}")

if __name__ == "__main__":
    # Read device names from eapi.conf
    with open('eapi.conf', 'r') as file:
        device_names = [line.strip().split()[1] for line in file if line.strip().startswith('connection')]

    # Retrieve running config for each device
    for device_name in device_names:
        retrieve_running_config(device_name)