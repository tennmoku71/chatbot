import requests
import json

#  APIキーの指定 - 以下を書き換えてください --- (※1)
apikey = "0b1f179a48ac27f22c849cb8088abb84"

# 天気を調べたい都市の一覧 --- (※2)
#cities = ["Tokyo,JP", "Kanagawa,JP", "Odawara,JP"]

# APIのひな型 --- (※3)
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}&lang=ja&units=metric"

# 温度変換( ケルビン→摂氏 ) --- (※4)
k2c = lambda k: k - 273.15


def show_weather(city_name):
    # AIPのURLを得る --- (※6)
    url = api.format(city=city_name, key=apikey)
    # 実際にAPIにリクエストを送信して結果を取得する --- (※6)
    r =requests.get(url)
    # 結果はJSON形式なのでデコードする --- (※7)
    date = json.loads(r.text)
    # 結果を画面に表示 --- (※8)
    sty = "今日の天気は " + date["weather"][0]["description"] + "。"
    sty = sty + "最低気温は " +  str(date["main"]["temp_min"]) + "度。"
    sty = sty + "最高気温は " +  str(date["main"]["temp_max"]) + "度。"
    sty = sty + "湿度は " + str(date["main"]["humidity"]) + "％。"
    
    return sty
