import requests
import json
import time

API_URL = "http://192.168.200.215:3000/api/v1/verifyDomain"

payload = {
    "bankDomainName": "testbankt1"
}

headers = {
    "Content-Type": "application/json"
}

time.sleep(3)

try:
    print("Sending POST request...")
    response = requests.post(API_URL, json=payload, headers=headers)
    response.raise_for_status()
    data = response.json()

    with open("local_api_output.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Success!")

except Exception as e:
    with open("local_api_output.json", "w") as f:
        f.write(str(e))
    raise e
