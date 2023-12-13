import requests
import json
import time
import random

api_url = "http://node.homesphere.tech/api/post-data"
key = 'your_key_here'
while True:
    try:
        # Generate random sensor data for the living room
        temperature_living_room = round(random.uniform(20.0, 30.0), 1)
        humidity_living_room = random.randint(30, 70)
        motion_sensor_living_room = random.choice([True, False])
        gas_levels_living_room = random.randint(0, 100)

        # Generate random sensor data for the dining and kitchen area
        temperature_kitchen = round(random.uniform(18.0, 28.0), 1)
        humidity_kitchen = random.randint(40, 80)
        motion_sensor_kitchen = random.choice([True, False])
        gas_levels_kitchen = random.randint(10, 90)

        # Generate random sensor data for the bedroom
        temperature_bedroom = round(random.uniform(18.0, 28.0), 1)
        humidity_bedroom = random.randint(40, 80)
        motion_sensor_bedroom = random.choice([True, False])
        gas_levels_bedroom = random.randint(10, 90)

        # Generate random sensor data for the bathroom
        temperature_bathroom = round(random.uniform(20.0, 30.0), 1)
        humidity_bathroom = random.randint(30, 70)
        motion_sensor_bathroom = random.choice([True, False])
        gas_levels_bathroom = random.randint(0, 100)

        # Data for the living room
        json_data_living_room = {
            "key": key,
            "room_name": "Living_Room",
            "sensor_data": {
                "temperature": temperature_living_room,
                "humidity": humidity_living_room,
                "motion_sensor": motion_sensor_living_room,
                "gas_levels": gas_levels_living_room
            },
            "devices": {
                "lights": [
                    {"name": "Living_Room_Ceiling_Light", "is_active": True},
                    {"name": "Living_Room_Lamp", "is_active": False},
                    # Add more lights as needed
                ],
                "plugs": [
                    {"name": "Living_Room_TV_Plug", "is_active": True},
                    {"name": "Living_Room_Fan_Plug", "is_active": False},
                    # Add more plugs as needed
                ]
            }
        }

        # Data for the dining and kitchen area
        json_data_kitchen = {
            "key": key,
            "room_name": "Dining_Kitchen_Area",
            "sensor_data": {
                "temperature": temperature_kitchen,
                "humidity": humidity_kitchen,
                "motion_sensor": motion_sensor_kitchen,
                "gas_levels": gas_levels_kitchen
            },
            "devices": {
                "lights": [
                    {"name": "Kitchen_Ceiling_Light", "is_active": True},
                    {"name": "Dining_Area_Pendant_Light", "is_active": True},
                    # Add more lights as needed
                ],
                "plugs": [
                    {"name": "Coffee_Maker_Plug", "is_active": True},
                    {"name": "Toaster_Plug", "is_active": False},
                    # Add more plugs as needed
                ]
            }
        }

        # Data for the bedroom
        json_data_bedroom = {
            "key": key,
            "room_name": "Bedroom",
            "sensor_data": {
                "temperature": temperature_bedroom,
                "humidity": humidity_bedroom,
                "motion_sensor": motion_sensor_bedroom,
                "gas_levels": gas_levels_bedroom
            },
            "devices": {
                "lights": [
                    {"name": "Bedroom_Ceiling_Light", "is_active": True},
                    {"name": "Bedside_Lamp", "is_active": False},
                    # Add more lights as needed
                ],
                "plugs": [
                    {"name": "Bedroom_Charger_Plug", "is_active": True},
                    {"name": "Bedroom_Fan_Plug", "is_active": False},
                    # Add more plugs as needed
                ]
            }
        }

        # Data for the bathroom
        json_data_bathroom = {
            "key": key,
            "room_name": "Bathroom",
            "sensor_data": {
                "temperature": temperature_bathroom,
                "humidity": humidity_bathroom,
                "motion_sensor": motion_sensor_bathroom,
                "gas_levels": gas_levels_bathroom
            },
            "devices": {
                "lights": [
                    {"name": "Bathroom_Ceiling_Light", "is_active": True},
                    {"name": "Bathroom_Vanity_Light", "is_active": False},
                    # Add more lights as needed
                ],
                "plugs": [
                    {"name": "Bathroom_Hairdryer_Plug", "is_active": True},
                    {"name": "Bathroom_Scale_Plug", "is_active": False},
                    # Add more plugs as needed
                ]
            }
        }

        # Send data for the living room
        response_living_room = requests.post(api_url, json=json_data_living_room)
        if response_living_room.status_code == 200:
            print("Data sent successfully for Living Room")
        else:
            print(f"Failed to send data for Living Room. Status code: {response_living_room.status_code}")

        # Send data for the dining and kitchen area
        response_kitchen = requests.post(api_url, json=json_data_kitchen)
        if response_kitchen.status_code == 200:
            print("Data sent successfully for Dining and Kitchen Area")
        else:
            print(f"Failed to send data for Dining and Kitchen Area. Status code: {response_kitchen.status_code}")

        # Send data for the bedroom
        response_bedroom = requests.post(api_url, json=json_data_bedroom)
        if response_bedroom.status_code == 200:
            print("Data sent successfully for Bedroom")
        else:
            print(f"Failed to send data for Bedroom. Status code: {response_bedroom.status_code}")

        # Send data for the bathroom
        response_bathroom = requests.post(api_url, json=json_data_bathroom)
        if response_bathroom.status_code == 200:
            print("Data sent successfully for Bathroom")
        else:
            print(f"Failed to send data for Bathroom. Status code: {response_bathroom.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

    time.sleep(10)
