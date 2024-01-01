# Python LEGO Move Hub Control

This is a Python project that provides an interface to control LEGO Boost hub and its peripherals using the `pylgbst` library. The project also integrates with MQTT for home automation purposes.

## Features

- Control LEGO Move hub and its peripherals.
- Handle device changes.
- Send and receive messages to/from the hub.
- Support for different types of hubs like MoveHub and SmartHub.
- Integration with MQTT for home automation.

## Requirements

- Python
- pip

## Installation

Clone the repository and navigate to the project directory. Install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Configuration
You need to provide the MAC address of your LEGO Boost hub and the MQTT connection parameters. These are set in the main.py file:
```python
mac_address = '9C:9A:C0:00:FB:F2'  # Replace with your LEGO Boost hub MAC address
mqtt_host = ''  # Replace with your MQTT host
mqtt_username = ''  # Replace with your MQTT username
mqtt_password = ''  # Replace with your MQTT password
```

## Usage
Run the main.py script to start the application. The script connects to the LEGO Boost hub and starts sending and receiving messages. It also connects to an MQTT broker and updates the state of a number entity and a sensor entity.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.  

## License
MIT
