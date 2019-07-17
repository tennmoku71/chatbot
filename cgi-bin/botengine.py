from janome.tokenizer import Tokenizer
import os, re, json, random

dict_file = "chatbot-data.json"
dic = {}
tokenizer = Tokenizer() # janome

import requests
import json

#  APIキーの指定 - 以下を書き換えてください --- (※1)
apikey = "0b1f179a48ac27f22c849cb8088abb84"

# 天気を調べたい都市の一覧 --- (※2)
#cities = ["Tokyo,JP", "Kanagawa,JP", "Odawara,JP"]

# APIのひな型 --- (※3)
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

# 温度変換( ケルビン→摂氏 ) --- (※4)
k2c = lambda k: k - 273.15


# 辞書に単語を記録する --- (*1)
def register_dic(words):
    global dic
    if len(words) == 0: return
    tmp = ["@"]
    for i in words:
        word = i.surface
        if word == "" or word == "\r\n" or word == "\n": continue
        tmp.append(word)
        if len(tmp) < 3: continue
        if len(tmp) > 3: tmp = tmp[1:]
        set_word3(dic, tmp)
        if word == "。" or word == "？":
            tmp = ["@"]
            continue
    # 辞書を更新するごとにファイルへ保存
    json.dump(dic, open(dict_file,"w", encoding="utf-8"))

# 三要素のリストを辞書として登録
def set_word3(dic, s3):
    w1, w2, w3 = s3
    if not w1 in dic: dic[w1] = {}
    if not w2 in dic[w1]: dic[w1][w2] = {}
    if not w3 in dic[w1][w2]: dic[w1][w2][w3] = 0
    dic[w1][w2][w3] += 1

# 都市名を引数に変換する
'''def convert_city(data):
    dic = {"東京" : "Tokyo,JP" , "名古屋" : "Nagoya,JP" , "大阪" : "Osaka,JP" , "福岡" : "Fukuoka,JP" , "札幌" : "Sapporo,JP"}

    return dic[data]'''


# 作文する --- (*2)
def make_sentence(head):
    if not head in dic: return ""
    ret = []
    if head != "@": ret.append(head)        
    top = dic[head]
    w1 = word_choice(top)
    w2 = word_choice(top[w1])
    ret.append(w1)
    ret.append(w2)
    while True:
        if w1 in dic and w2 in dic[w1]:
            w3 = word_choice(dic[w1][w2])
        else:
            w3 = ""
        ret.append(w3)
        if w3 == "。" or w3 == "？" or w3 == "": break
        w1, w2 = w2, w3
    return "".join(ret)

def word_choice(sel):
    keys = sel.keys()
    return random.choice(list(keys))

def show_weather(city_name):
    # AIPのURLを得る --- (※6)
    url = api.format(city=city_name, key=apikey)
    # 実際にAPIにリクエストを送信して結果を取得する --- (※6)
    r =requests.get(url)
    # 結果はJSON形式なのでデコードする --- (※7)
    date = json.loads(r.text)
    # 結果を画面に表示 --- (※8)
    sty = "今日の天気は" + date["weather"][0]["description"] + "。"
    sty = sty + "最低気温は" +  str(k2c(date["main"]["temp_min"])) + "度。"
    sty = sty + "最高気温は" +  str(k2c(date["main"]["temp_max"])) + "度。"
    sty = sty + "湿度は" + str(date["main"]["humidity"]) + "％。"
    
    return sty


# チャットボットに返答させる --- (*3)
def make_reply(text):
    # まず単語を学習する
    if text[-1] != "。": text += "。"
    words = tokenizer.tokenize(text)
    register_dic(words)
    city_dic = {"東京" : "Tokyo,JP" , 
            "名古屋" : "Nagoya,JP" , 
            "大阪" : "Osaka,JP" , 
            "福岡" : "Fukuoka,JP" , 
            "札幌" : "Sapporo,JP"}
    
    # 辞書に単語があれば、そこから話す
    for w in words:
        face = w.surface
        ps = w.part_of_speech.split(',')[0]
        if ps == "感動詞":
            return face + "。"
        if ps == "名詞" or ps == "形容詞":
            if face in city_dic :
                    return show_weather(city_dic[face])
            if face in dic: return make_sentence(face) 
    return make_sentence("@")

# 辞書があれば最初に読み込む
if os.path.exists(dict_file):
    dic = json.load(open(dict_file,"r"))
    