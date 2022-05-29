import json
import requests
import datetime

QIWI_API_SECRET_KEY = ''


def create_bill(userid, amount):
    expdate = str(datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(minutes=30), "%Y-%m-%dT%H:%M:%S")) + '+03:00'

    params = {
        "amount": {
            "currency": "RUB",
            "value": f"{amount}"
        },
        "comment": "Пополнение счёта Flowers shop",
        "expirationDateTime": expdate
    }

    headers = {
        'content-type': 'application/json',
        'accept' : 'application/json',
        'Authorization' : f'Bearer {QIWI_API_SECRET_KEY}'
    }

    responce = requests.put(url = f'https://api.qiwi.com/partner/bill/v1/bills/fwshop_{userid}' ,data = json.dumps(params), headers = headers)
    pay_url = json.loads(responce.text)['payUrl']

    return (pay_url)