print("AQI Simple Reflex Agent\n")

def read_sensor_data(filename):
    data = {}

    with open(filename, 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            data[key] = float(value)

    return data


def calculate_aqi(data):
    pm25 = data.get("PM2.5", 0)

    if pm25 <= 50:
        return "Good"
    elif pm25 <= 100:
        return "Satisfactory"
    elif pm25 <= 200:
        return "Moderate"
    elif pm25 <= 300:
        return "Poor"
    elif pm25 <= 400:
        return "Very Poor"
    else:
        return "Severe"


data = read_sensor_data("aqi_data.txt")

print("Sensor Data:", data)

aqi_status = calculate_aqi(data)

print("\nAQI Category:", aqi_status)