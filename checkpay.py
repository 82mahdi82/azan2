import requests

# مقادیر مورد نیاز شما
merchant_id = '7aa08ed2-ff34-44d4-867b-d918676f856f'
authority = 'A00000000000000000000000000527061758'

# URL آدرس API زرین پال
url = 'https://api.zarinpal.com/pg/v4/payment/verify.json'

# پارامتر‌های ارسالی به زرین پال
payload = {
    'merchant_id': merchant_id,
    'authority': authority,
    'amount': 10000  # مبلغ به ریال
}

# درخواست بررسی وضعیت پرداخت
response = requests.post(url,json=payload)

if response.status_code == 200:
    # اگر درخواست با موفقیت انجام شد
    response_data = response.json()
    print(response_data)
    if response_data['data']['code'] == 100:
        # پرداخت موفق بوده است
        print('Payment is verified.')
    else:
        # پرداخت ناموفق بوده است
        print('Payment verification failed.')
else:
    # در صورت خطا
    print('Request failed with status code:', response.status_code)
