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
