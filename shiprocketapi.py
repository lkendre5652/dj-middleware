import requests
import json

# Authentication request
auth_url = "https://apiv2.shiprocket.in/v1/external/auth/login"
auth_payload = json.dumps({
    "email": "pavan.gaikwad@ikf.co.in",
    "password": "Laxman@123"
})
auth_headers = {
    'Content-Type': 'application/json'
}
auth_response = requests.post(auth_url, headers=auth_headers, data=auth_payload)
auth_data = json.loads(auth_response.text)
print( auth_data)

# Check if authentication was successful
if 'token' in auth_data:
    access_token = auth_data['token']

    # API request
    api_url = 'https://apiv2.shiprocket.in/v1/external/courier/serviceability/'
    api_headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }
    api_payload = {
        # "email": "accounts@myrahspa.com",
        # "password": "Accounts@2023"
        # Add any additional data required for the courier/serviceability endpoint
    }
    api_response = requests.get(api_url, headers=api_headers, data=json.dumps(api_payload))
    print(api_response.text)
else:
    print("Authentication failed. Check credentials.")
