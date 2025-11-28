import requests
import json
import time

API_URL = " http://192.168.200.215:3000/api/v1/verifyDomain"

# Wait for API to boot up
time.sleep(3)

try:
    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()

    with open("local_api_output.json", "w") as f:
        json.dump(data, f, indent=4)

    print("API test successful!")
    print("Saved to local_api_output.json")

except Exception as e:
    with open("local_api_output.json", "w") as f:
        f.write(str(e))
    raise e
