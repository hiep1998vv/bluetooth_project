import bluetooth

def get_rssi(address):
    try:
        services = bluetooth.find_service(address=address)
        if len(services) > 0:
            for svc in services:
                port = svc["port"]
                name = svc["name"]
                host = svc["host"]
                rssi = bluetooth.lookup_name(address, timeout=5)
                if rssi:
                    print(f"RSSI for {name} ({address}): {rssi}")
                    return rssi
                else:
                    print(f"Could not retrieve RSSI for {name} ({address})")
    except Exception as e:
        print(f"Error: {e}")

# Replace '00:00:00:00:00:00' with the Bluetooth device's MAC address
device_mac_address = '00:00:00:00:00:00'
get_rssi(device_mac_address)

# hcitool with linux
import subprocess

def get_rssi(device_mac_address):
    try:
        output = subprocess.check_output(['hcitool', 'rssi', device_mac_address])
        rssi = int(output.decode().split('RSSI return value: ')[1])
        print(f"RSSI for device ({device_mac_address}): {rssi}")
        return rssi
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

device_mac_address = '00:00:00:00:00:00'  # Replace with your device's MAC address
get_rssi(device_mac_address)


# using pygatt 
import pygatt
import time

def get_rssi(device_mac_address):
    try:
        adapter = pygatt.GATTToolBackend()
        adapter.start()
        device = adapter.connect(device_mac_address)
        time.sleep(1)  # Give some time for RSSI to stabilize
        rssi = device.get_rssi()
        device.disconnect()
        adapter.stop()
        print(f"RSSI for device ({device_mac_address}): {rssi}")
        return rssi
    except Exception as e:
        print(f"Error: {e}")

device_mac_address = '00:00:00:00:00:00'  # Replace with your device's MAC address
get_rssi(device_mac_address)


# using bluepy
from bluepy.btle import Scanner

def get_rssi(device_mac_address):
    try:
        scanner = Scanner()
        devices = scanner.scan(2.0)  # Scan for 2 seconds
        for dev in devices:
            if dev.addr == device_mac_address:
                print(f"RSSI for device ({device_mac_address}): {dev.rssi}")
                return dev.rssi
        print(f"Device ({device_mac_address}) not found in scan results")
    except Exception as e:
        print(f"Error: {e}")

device_mac_address = '00:00:00:00:00:00'  # Replace with your device's MAC address
get_rssi(device_mac_address)

