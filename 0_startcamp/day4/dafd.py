# 네이버 Papago NMT API 예제
import os
import sys
import urllib.request

def translate_lang():
    client_id = "HnR6v1IdNhYJaslni_5v"
    client_secret = "ZBdGUtNIEa"
    #encText = urllib.parse.quote("번역할 문장을 입력하세요")
    data = "source=es&target=ko&text=quiero tomar una cerveza."
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
    return 