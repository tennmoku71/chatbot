# -*- coding: utf-8 -*-

import random
import requests
import json
import datetime

def conv_birth_to_conste(birthday="6.16"):
    a = [u'山羊座', u'水瓶座', u'魚座', u'牡羊座', u'牡牛座', u'双子座', u'蟹座', u'獅子座', u'乙女座', u'天秤座', u'蠍座', u'射手座']
    b = [20, 19, 20, 20, 20, 21, 23, 23, 23, 23, 22, 22]
    l = birthday.split(".")
    m = int(l[0])
    d = int(l[1])
    #print(a[ m-13 + (d > b[m-1]) ]) 
    return a[ m-13 + (d > b[m-1]) ]
#conv_birth_to_conste()

def tell_fortune(birthday="6.16"):
    conste = conv_birth_to_conste(birthday)

    date = datetime.datetime.today().strftime("%Y/%m/%d")

    seiza_by_index = {
        '牡羊座': 0,
        '牡牛座': 1,
        '双子座': 2,
        '蟹座': 3,
        '獅子座': 4,
        '乙女座': 5,
        '天秤座': 6,
        '蠍座': 7,
        '射手座': 8,
        '山羊座': 9,
        '水瓶座': 10,
        '魚座': 11,
    }

    index = seiza_by_index[conste]

    # http://api.jugemkey.jp/api/horoscope/year/month/day の形式
    res = requests.get(url='http://api.jugemkey.jp/api/horoscope/free/'+ date)
    data = json.loads(res.text)

    keys =list(seiza_by_index.keys())
    seiza = keys[index]

    color=data['horoscope'][date][index]['color']
    content=data['horoscope'][date][index]['content']

    #print("{}のあなた。{}ラッキーカラーは{}。".format(seiza,content,color))
    return "{}のあなた。{}ラッキーカラーは{}。".format(seiza,content,color)



if __name__ == "__main__":

    print(tell_fortune("2.1"))
