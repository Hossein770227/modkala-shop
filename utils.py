import requests


def send_otp_code(phone_number, code):
    url = 'https://api.limosms.com/api/sendpatternmessage'
    message = [f"{code}"]
    myobj = {'OtpId' :'593',
    'ReplaceToken' : message,
    'MobileNumber' : f'{phone_number}'}
    x = requests.post(url, json = myobj, headers = {"ApiKey":"acd07e6c-ffb8-434e-9875-42ac71e1acba"})
    print(x.text)
    # x = requests.post(url, json = myobj, headers = {"ApiKey": "acd07e6c-ffb8-434e-9875-42ac71e1acba"})
