# 181220 summary

## 1. HTML

* 마크업 언어
  * 역할 지정 - 보여지는걸 생각해서 코딩하면 안된다
  * h1, h2, h3 태그를 글씨 크기로 구분하면 안됨 (h1은 가장 중요한 제목에 주는 태그)
* 보여지는 영역은 css로 해결

## 2. 로또 풀이

* 다른 풀이 방법 

```python
count = 0
for my_number in my_numbers:
    for real_number in real_numbers:
        if my_number == real_number:
            count +=1
print(count)

if count == 6:
    print(1)
elif count == 5 and bonus in my_numbers:
    print(2)
    ...
```

* 집합 자료형
  * 'unordered' collection
* 함수 (2*2)
  * return 값이 있거나 / 없거나
    * return 값 있다 : a = sorted([3, 2, 1])
    * 없다 : b = [3, 2, 1].sort()
    * return 값이 없다 != 동작하지 않는다
  * 인자가 있거나 / 없거나
* 컨벤션 = 통상적으로 지키는 것,  관습, 안지킨다고 코드가 무너지거나 하진 않음.
* 리팩토링 = 기능이나 성능 차이는 없지만, 코드를 깔끔하게 다듬고, 변수 이름을 알아보기 쉽게, 들여쓰기 등등 을 하는 작업

## 3. 로또 함수화

```python
import requests
import random

#리팩토링 한 코드 -> 보기 쉽게 함수로 만듦
#define pick_lotto
def pick_lotto():
    numbers = random.sample(range(1, 46), 6)
    return numbers

pick_numbers = pick_lotto()
print(pick_numbers)

#define get_lotto : 로또 홈페이지에서 api를 통해 n 회차 데이터를 받아오고 정제해서 번호 추출
def get_lotto(draw_no):
    url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo={}'.format(draw_no)
    lotto_data = requests.get(url, verify=False).json() #parsing 기존 str을 dict로 바꿈 (해석)
    numbers = []
    for key, value in lotto_data.items():
        if 'drwtNo' in key:
            numbers.append(value)
    bonus = lotto_data['bnusNo']
    return {'numbers' : numbers, 'bonus' : bonus}

real_numbers = get_lotto(837)
print(real_numbers)	

#이전 코드
#real_numbers = get_lotto()
#result = am_i_lucky(pick_numbers, real_numbers)


# url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

# response = requests.get(url, verify=False)
# lotto_data = response.json() #parsing 기존 str을 dict로 바꿈 (해석)

# real_numbers = []
# for key, value in lotto_data.items():
#     if 'drwtNo' in key:
#         real_numbers.append(value)

# real_numbers.sort()
# bonus_number = lotto_data['bnusNo']

# print(real_numbers)
# print(pick_numbers)

# a = set(real_numbers)
# b = set(pick_numbers)
# c = len(a.intersection(b))
```

* editor 에서 alt 누르면 다중 드래그 가능

## 4. API server 만들기

* $ = prompt 입력할 수 있는 상태
* flask run = 서버 킨다 , ctrl + c  끄기
* from flask import Flask, jsonify
  * jsonify()
* flask run -h 0.0.0.0 -p 8080

```python
from flask import Flask, jsonify
from random import sample

app = Flask(__name__)

@app.route("/")
def index():
    return 'Happy Hacking'
    
@app.route("/hi")
def hi():
    return 'Hello SSAFY'
    
@app.route("/pick_lotto")
def pick_lotto():
    return jsonify(sample(range(1, 46), 6))
    
@app.route("/get_lotto")
def get_lotto():
    data = {
        'numbers': [1, 2, 3, 4, 5, 6],
        'bonus': 7
    }
    return jsonify(data)
```



내가 메세지 보냄 -> 텔레그램 서버 -> 플라스크 서버 -> 텔레그램 서버 -> 메세지