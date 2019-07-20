from janome.tokenizer import Tokenizer
import os, re, json, random
from datetime import datetime　# りなんが追加
from fortune import tell_fortune　# くれりんが追加
from weather import show_weather  # 天気のモジュール

dict_file = "chatbot-data.json"
dic = {}
tokenizer = Tokenizer() # janome

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

# チャットボットに返答させる --- (*3)
def make_reply_original(text):
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
            # 登録された地名が辞書 city_dic にあれば、その天気を返す
            if face in city_dic :
                    return show_weather(city_dic[face])
            if face in dic: return make_sentence(face) 
    return make_sentence("@")

def make_reply(text):
    # 文章に "占い." が含まれていたら日付と時刻を返す。（くれりんが追加）
    if "占い." in text:
        text1 = text.replace("占い.", "")
        return tell_fortune(text1)
    # 文章に "何時" が含まれていたら日付と時刻を返す。（りなんが追加）
    if "何時" in text: 
        date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        return date_time
    # まず単語を学習する
    if text[-1] != "。": text += "。"
    words = tokenizer.tokenize(text)
    register_dic(words)
    # 形態素解析して分割した複数の単語についてループする
    for w in words:
        # 単語
        face = w.surface
        # 品詞
        ps = w.part_of_speech.split(',')[0]
        if ps == "感動詞":
            return face + "。"
        if ps == "名詞" or ps == "形容詞":
            # 時刻、日付、曜日　が含まれていたら現在の値を返す。（りなんが追加）
            if face=="時刻":
                date_time = datetime.now().strftime("%H:%M:%S")
                return date_time
            if face=="日付":
                a_date = datetime.now().strftime("%Y年%m月%d日")
                return a_date
            if face=="曜日":
                weekday = datetime.now().weekday()
                week_dic= {0:"月曜日",1:"火曜日",2:"水曜日",3:"木曜日",4:"金曜日",5:"土曜日",6:"日曜日"}
                return week_dic[weekday]
            # 辞書に単語があれば、そこから話す
            if face in dic:
                return make_sentence(face)
    return make_sentence("@")

# 辞書があれば最初に読み込む
if os.path.exists(dict_file):
    dic = json.load(open(dict_file,"r"))
    