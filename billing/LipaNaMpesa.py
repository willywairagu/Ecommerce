import requests
import base64
from billing import keys
from datetime import datetime
from requests.auth import HTTPBasicAuth

# Getting our timestamp
time = datetime.now()
formatted_time = time.strftime("%Y%m%d%H%M%S")


# Getting our password
def generate_password(f_time):
    data_to_encode = keys.business_shortCode + keys.lipa_na_mpesa_passKey + f_time
    encoded = base64.b64encode(data_to_encode.encode())
    decoded_password = encoded.decode('utf-8')
    return decoded_password


# Access Token
def generate_access_token():
    consumer_key = keys.consumer_key
    consumer_secret = keys.consumer_secret
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

    json_response = r.json()
    my_access_token = json_response['access_token']
    return my_access_token


def lipa_na_mpesa(number):
    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}

    request = {
        "BusinessShortCode": keys.business_shortCode,
        "Password": generate_password(formatted_time),
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "5",
        "PartyA": number,
        "PartyB": keys.business_shortCode,
        "PhoneNumber": number,
        "CallBackURL": "https://fullstackdjango.com/lipanampesa/",
        "AccountReference": "wairagu",
        "TransactionDesc": "testing"
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)


# lipa_na_mpesa()