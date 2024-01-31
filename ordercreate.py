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

    url = "https://apiv2.shiprocket.in/v1/external/courier/serviceability/"

    payload = json.dumps({
    "pickup_postcode": 411039,
    "delivery_postcode": 122002,
    "weight": 2,
    "cod": 0
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer'+ access_token
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
