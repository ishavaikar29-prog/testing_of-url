import requests
import json
import time

API_URL = "https://dev.app.creditos.in/api/v1/verifyDomain"

# Body should be EXACTLY what you put in Postman (raw JSON)
payload = {
    "bankDomainName": "testbankt1"
}

# Raw JSON MUST have this header
headers = {
    "Content-Type": "application/json"
}

time.sleep(3)

try:
    print("Sending POST...")
    response = requests.post(API_URL, json=payload, headers=headers)
    print("Status code:", response.status_code)
    print("Response text:", response.text)

    response.raise_for_status()

    data = response.json()

    # Save API response in artifact file
    with open("local_api_output.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Saved as artifact!")

except Exception as e:
    with open("local_api_output.json", "w") as f:
        f.write(str(e))
    raise e
