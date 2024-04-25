import requests


def payment(amount_int):
# مقادیر مورد نیاز شما
    merchant_id = '7aa08ed2-ff34-44d4-867b-d918676f856f'
    amount = amount_int  # مبلغ به ریال
    description = 'payment'

    # URL آدرس API زرین پال
    url = 'https://api.zarinpal.com/pg/v4/payment/request.json'

    # پارامتر‌های ارسالی به زرین پال
    payload = {
        'merchant_id': merchant_id,
        'amount': amount,
        'description': description,
        'callback_url': 'https://novinzaban.com/',
        "metadata": {"mobile": "09926668326"}
    }

    # درخواست ایجاد پرداخت
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        # اگر درخواست با موفقیت انجام شد
        response_data = response.json()
        # if 'errors' in response_data:
        #     print('Error occurred:', response_data['errors'])
        # else:
        print(response_data)
            # لینک پرداخت ایجاد شده
        payment_url = 'https://www.zarinpal.com/pg/StartPay/' + response_data["data"]['authority']
        print('Payment URL:', payment_url)
        return {"url":payment_url,"authority":response_data["data"]['authority']}
    else:
        # در صورت خطا
        print('Request failed with status code:', response.status_code)
