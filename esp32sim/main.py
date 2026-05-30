import requests
import random
import time
from datetime import datetime
from zoneinfo import ZoneInfo


API_URL = "https://apiforsmartplanter.onrender.com/sensor_readings"

while True:
    data = {
    "moisture": random.randint(20, 80),
    "ph": round(random.uniform(5.5, 7.5), 1),
    "is_day": random.choice([True, False]),
    "timestamp": datetime.now(
        ZoneInfo("Asia/Kolkata")
    ).isoformat()
}
    try:
        response = requests.post(API_URL, json=data)
        print(f"Sent: {data}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print("Error:", e)

    time.sleep(5)