import requests
import json
import time

API_URL = "http://192.168.200.215:3000/api/v1/verifyDomain"   # your endpoint

# Your JSON body (VALID Python dict)
API_Body = {
    "bankDomainName": "testbankt1"
}



time.sleep(3)  # wait for local API to start

try:
    print(f"Sending POST request to: {API_URL}")
    print(f"API Body: {API_Body}")

    response = requests.post(API_URL, json=API_Body)
    response.raise_for_status()

    data = response.json()

    # Save API response in artifact file
    with open("local_api_output.json", "w") as f:
        json.dump(data, f, indent=4)

    print("API test successful!")
    print("Saved to local_api_output.json")

except Exception as e:
    with open("local_api_output.json", "w") as f:
        f.write(str(e))
    raise e
