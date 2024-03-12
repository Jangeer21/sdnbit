import pyeapi

def get_eos_version(device_ip, username, password):
    # Create the connection to the EOS device
    connection = pyeapi.connect(
        transport='https',
        host=device_ip,
        username=username,
        password=password,
        return_node=True,
    )

    # Send the "show version" command
    response = connection.enable(['show version'])

    # Extract and print the result
    version_output = response[0]['result']['version']
    print('Version -> ', version_output)

if __name__ == "__main__":
    # Replace these values with your EOS device's IP, username, and password
    eos_device_ip = '192.168.0.3'
    eos_username = 'arista'
    eos_password = 'arista'

    get_eos_version(eos_device_ip, eos_username, eos_password)