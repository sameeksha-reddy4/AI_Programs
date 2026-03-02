print("AQI Simple Reflex Agent\n")

# ---------- SENSOR ----------
def read_sensor_data(filename):
    data = {}
    with open(filename, 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            data[key] = float(value)
    return data


# ---------- AQI RULES ----------
def pollutant_aqi(value):
    if value <= 50:
        return "Good"
    elif value <= 100:
        return "Satisfactory"
    elif value <= 200:
        return "Moderate"
    elif value <= 300:
        return "Poor"
    elif value <= 400:
        return "Very Poor"
    else:
        return "Severe"


# ---------- REFLEX AGENT ----------
def evaluate_aqi(data):

    categories = []

    for pollutant, value in data.items():
        categories.append(pollutant_aqi(value))

    # Worst case determines AQI
    order = ["Good", "Satisfactory", "Moderate",
             "Poor", "Very Poor", "Severe"]

    return max(categories, key=lambda x: order.index(x))


data = read_sensor_data("aqi_data.txt")

print("Sensor Data:", data)

aqi_status = evaluate_aqi(data)

print("\nOverall AQI Category:", aqi_status)