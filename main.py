
# coding=utf-8
import asyncio
import threading
import time

from ha_mqtt_discoverable import Settings
from ha_mqtt_discoverable.sensors import Number, NumberInfo, Sensor, SensorInfo
from paho.mqtt.client import Client, MQTTMessage
from pylgbst import *
from pylgbst.hub import MoveHub

log = logging.getLogger("demo")

def set_power(movehub: MoveHub, numberEntity: Number, power: int):
    movehub.motor_A.power(power / 100)
    numberEntity.set_value(power)

# Press the green button in the gutter to run the script.
async def connect_to_hub(macAddress: str):
    connection = get_connection_bleak(hub_mac=macAddress)
    hub = MoveHub(connection)
    return hub
async def main():
    global hub
    logging.basicConfig(level=logging.INFO, format='%(relativeCreated)d\t%(levelname)s\t%(name)s\t%(message)s')
    mac_address = '9C:9A:C0:00:FB:F2'
    mqtt_host = ''
    mqtt_username = ''
    mqtt_password = ''
    try:
        while True:
            try:
                hub = await connect_to_hub(mac_address)
                break
            except Exception as e:
              pass

        macAsId = mac_address.replace(":", "")
        mqtt_settings = Settings.MQTT(host=mqtt_host,
                                      username=mqtt_username,
                                      password=mqtt_password,
                                      client_name='movehub-connect')
        # Information about the `number` entity.
        number_info = NumberInfo(name="train-power-" + macAsId, min=-100, max=100, mode="slider", step=10)

        settings = Settings(mqtt=mqtt_settings, entity=number_info)

        def power_update(client: Client, user_data, message: MQTTMessage):
            number = int(message.payload.decode())
            logging.info(f"Received {number} from HA")
            set_power(hub, speed_number, number)

        speed_number = Number(settings, lambda client, user_data, message: power_update(client, user_data, message))
        speed_number.set_value(0)

        battery_info = SensorInfo(name="train-battery-" + macAsId, unique_id="train-battery-" + macAsId, unit_of_measurement="V", value_template="{{ value|float }}")

        battery_settings = Settings(mqtt=mqtt_settings, entity=battery_info)
        battery_sensor = Sensor(battery_settings)
        while True:
            battery_sensor.set_state(hub.voltage.voltage)
            time.sleep(30)
    finally:
        if hub:
            hub.disconnect()

asyncio.run(main())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
