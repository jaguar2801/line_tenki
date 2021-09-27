import requests
import tenki


acc_token='取得したトークン'

def send_line(msg):
    # サーバーに送るパラメータを用意 --- (*2)
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + acc_token}
    payload = {'message': msg}
    requests.post(url, headers=headers, params=payload)
text=tenki.get()
def today_print(text):
    
    location=text['location']
    date=text['today']['date']
    weather=text['today'][ 'forecasts'][0]['weather']
    high_temp=text['today'][ 'forecasts'][0]['high_temp']
    low_temp=text['today'][ 'forecasts'][0]['low_temp']
    rain_probability=text['today'][ 'forecasts'][0]['rain_probability']
    return [location,date,weather,high_temp,low_temp,str(rain_probability)]

def tomorrow_print(text):
    location=text['location']
    date=text['tomorrow']['date']
    weather=text['tomorrow'][ 'forecasts'][0]['weather']
    high_temp=text['tomorrow'][ 'forecasts'][0]['high_temp']
    low_temp=text['tomorrow'][ 'forecasts'][0]['low_temp']
    rain_probability=text['tomorrow'][ 'forecasts'][0]['rain_probability']
    return [location,date,weather,high_temp,low_temp,str(rain_probability)]

if __name__=='__main__':
    send_line('-----'+today_print(text)[0]+'------\n'
    '今日　　'+today_print(text)[1]+'\n'
    '天気　　'+today_print(text)[2]+'\n'
    '最高気温'+today_print(text)[3]+'\n'
    '最低気温'+today_print(text)[4]+'\n'
    '降水確率'+today_print(text)[5]+'\n'
    '-------'+today_print(text)[0]+'-------\n'
    '明日  　'+tomorrow_print(text)[1]+'\n'
    '天気　　'+tomorrow_print(text)[2]+'\n'
    '最高気温'+tomorrow_print(text)[3]+'\n'
    '最低気温'+tomorrow_print(text)[4]+'\n'
    '降水確率'+tomorrow_print(text)[5]+'\n'
    )
    print('ok')


