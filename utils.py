import requests
def send_otp_code(phone_number, code):
    url = 'https://api.limosms.com/api/sendpatternmessage'
    message = [f"  {code} خوش امدید کد تایید "]
    myobj = {'OtpId' :'593',
    'ReplaceToken' : message,
    'MobileNumber' : phone_number}
    x = requests.post(url, json = myobj, headers = {"ApiKey": "779445eb-0af4-4e94-909a-4fe2a1a69f5f"})
