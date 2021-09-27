import re
import requests
from bs4 import BeautifulSoup
import json

def main(url):
    # bs4でパース
    s = soup(url)

    dict = {}

    # 予測地点
    l_pattern = r"(.+)の今日明日の天気"
    l_src = s.title.text
    dict['location'] = re.findall(l_pattern, l_src)[0]
    #print(dict['location'] + "の天気")

    soup_tdy = s.select('.today-weather')[0]
    soup_tmr = s.select('.tomorrow-weather')[0]

    dict["today"] = forecast2dict(soup_tdy)
    dict["tomorrow"] = forecast2dict(soup_tmr)

    # JSON形式で出力
    return dict

def soup(url):
    r = requests.get(url)
    html = r.text.encode(r.encoding)
    return BeautifulSoup(html, 'lxml')

def forecast2dict(soup):
    data = {}

    # 日付処理
    d_pattern = r"(\d+)月(\d+)日\(([土日月火水木金])+\)"
    d_src = soup.select('.left-style')
    date = re.findall(d_pattern, d_src[0].text)[0]
    data["date"] = "%s-%s(%s)" % (date[0], date[1], date[2])
    #print("=====" + data["date"] + "=====")

    # ## 取得
    weather           = soup.select('.weather-telop')[0]
    high_temp         = soup.select("[class='high-temp temp']")[0]
    high_temp_diff    = soup.select("[class='high-temp tempdiff']")[0]
    low_temp          = soup.select("[class='low-temp temp']")[0]
    low_temp_diff     = soup.select("[class='low-temp tempdiff']")[0]
    rain_probability  = soup.select('.rain-probability > td')
    wind_wave         = soup.select('.wind-wave > td')[0]

    # ## 格納
    data["forecasts"] = []
    forecast = {}
    forecast["weather"] = weather.text.strip()
    forecast["high_temp"] = high_temp.text.strip()
    forecast["high_temp_diff"] = high_temp_diff.text.strip()
    forecast["low_temp"] = low_temp.text.strip()
    forecast["low_temp_diff"] = low_temp_diff.text.strip()
    every_6h = {}
    for i in range(4):
        time_from = 0+6*i
        time_to   = 6+6*i
        itr       = '{:02}-{:02}'.format(time_from,time_to)
        every_6h[itr] = rain_probability[i].text.strip()
    forecast["rain_probability"] = every_6h
    forecast["wind_wave"] = wind_wave.text.strip()

    data["forecasts"].append(forecast)

    list_=[
        "天気              ： " + forecast["weather"] + "\n"
        "最高気温(C)       ： " + forecast["high_temp"] + "\n"
        "最高気温差(C)     ： " + forecast["high_temp_diff"] + "\n"
        "最低気温(C)       ： " + forecast["low_temp"] + "\n"
        "最低気温差(C)     ： " + forecast["low_temp_diff"] + "\n"
        "降水確率[00-06]   ： " + forecast["rain_probability"]['00-06'] + "\n"
        "降水確率[06-12]   ： " + forecast["rain_probability"]['06-12'] + "\n"
        "降水確率[12-18]   ： " + forecast["rain_probability"]['12-18'] + "\n"
        "降水確率[18-24]   ： " + forecast["rain_probability"]['18-24'] + "\n"
        "風向              ： " + forecast["wind_wave"] + "\n"
    ]
    #print(data)

    return data

def get():
    URL = '好きな土地のurl'
    return main(URL)
    