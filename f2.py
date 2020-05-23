token='5ec0b8daa9797d000a049ff5.YK6oydwRbf1621224538535.116489331385292670685'
my_id='5ec0b8daa9797d000a049ff5'
cookie='G_ENABLED_IDPS=google; __cfduid=dcdfdb7e8b05136695eca1c6b077ae1fe1589775965'
import requests
import json
import time
import winsound
import keyboard
import numpy as np
frequency = 500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
ac=['girl2'for i in range(12)]+['train2'for i in range(7)]+['fish2'for i in range(7)]+['girl2'for i in range(7)]+['fish2'for i in range(7)]+['girl2'for i in range(7)]+['fish2'for i in range(99)]
def str2obj(s,s1=';',s2='='):
    li=s.split(s1)
    res={}
    for kv in li:
        li2=kv.split(s2)
        if len(li2)>1:
            res[li2[0]]=li2[1]
    return res
def beep():
    t=0
    while True:
        if t%20==0:
            winsound.Beep(frequency, duration)
        if keyboard.is_pressed('q'):
            return
        else:
            time.sleep(1)
        t+=1
def action():
    url='https://mykirito.com/api/my-kirito'
    headers='''
accept: application/json, text/plain, */*
accept-encoding: gzip, deflate
accept-language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7
referer: https://mykirito.com/
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36
'''
    headers=str2obj(headers,'\n',': ')
    headers['token']=token
    headers['cookie']=cookie
    while True:
        jsonData=requests.get(url,headers=headers)
        try:
            data=json.loads(jsonData.text)
            break
        except:
            time.sleep(10)
    lv=data['lv']
    url='https://mykirito.com/api/my-kirito/doaction'
    headers='''
accept: application/json, text/plain, */*
accept-encoding: gzip, deflate
accept-language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7
content-type: application/json;charset=UTF-8
origin: https://mykirito.com
referer: https://mykirito.com/
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36
'''
    headers=str2obj(headers,'\n',': ')
    headers['token']=token
    headers['cookie']=cookie
    params={'action': ac[lv-1]}
    while True:
        jsonData=requests.post(url,json.dumps(params),headers=headers)
        print(jsonData.text)
        if 'try again'in jsonData.text or'還在冷卻中'in jsonData.text or 'Rate'in jsonData.text or '伺服器承載過高'in jsonData.text:
            time.sleep(10)
        elif '需進行防機器人驗證'in jsonData.text:
            print('行動防掛')
            beep()
            print('OK')
            return
        elif '死亡'in jsonData.text:
            print('轉生')
            beep()
            print('OK')
        else:
            break
    data=json.loads(jsonData.text)
    if data['gained']['prevLV']!=data['gained']['nextLV']:
        gain=np.load('gain.npy',allow_pickle=True)
        gain[data['gained']['nextLV']][ac[lv-1]]=data['gained']
        np.save('gain.npy',gain)
    print(data['message'])

while True:
    action()
    time.sleep(100)
