# 181218 수업정리

## 1. 개발환경 설정

* chocolatey
  * 윈도우 패키지 매니저
* python -v 3.6.7
* git
  * Version Control System
* vscode
  * Code Editor
* chrome
  * Browser

## 2. List

100 / 10

10.0 실수 출력

인덱스

list[-1] :  뒤에서부터 인덱싱

앞에서부터 0, 1, 2, 3 , 4

뒤에서부터 -1, -2, -3, -4, -5

searching & sorting

### 리스트 연산 (리스트 + 리스트)

```python
team = [
    'john', 10000,
    'neo', 100,
    'tak', 40500
]

new_member = ['js', 10]

team = team + new_member
team += new_member # 위에랑 같은말 
print(team)
['john', 10000, 'neo', 100, 'tak', 40500, 'js', 10]
```



### 리스트 추출하기

```python
mcu = [
    ['ironman', 'captain america', 'dr.strange'], 
    ['xmen', 'deadpool'], 
    ['spiderman']
]
disney = mcu[0]
dr_strange = disney[2]
dr_strange = mcu[0][2]
```

`'dr.strange'`에 접근하려면 어떻게 해야할까?

`[0]`처럼 인덱스 이용

`[1:10]`처럼 잘라내기 

### type casting

`list(range(1, 46)` = [1, 2, 3, ..., 45]

`int('123')`

`str()`



## 3. Dict

```python
my_info = {
    'name' : 'Jun',
    'job' : 'hacker',
    'age' : '30',
    'moboile' : '01040033223',
    'email' : 'parkbj7461@gmail.com'
}
```

`my_dict = {'key' : 'value', key' : 'value', key' : 'value', key' : 'value'}`

`my_dict['key']`



## 4. Function

```python
print('123')
len('hi')
del()
type('a')

scores = [45, 60, 89, 77]
high_score = max(scores)
round() #반올림
round(1.876, 2) 

lowest_score = min(scores)

first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

full = first + second

full_sorted = sorted(full)

reverse_sorted = sorted(full, reverse = True)
```

## 5. Method

```python
my_list = [4, 7, 9, 1, 3, 6]
#최대/최소
max(my_list)
min(my_list)
#특정 요소의 인덱스
my_list.index()
#리스트를 뒤집으려면?
my_list.reverse()

dust = 100 # <class: int>
lang = 'python' # str
samsung = ['elec', 'sds', 's1'] # list

samsung.index('sds')

lang.capitalize() #첫글자 대문자로 바꿔라
lang.replace('on', 'off') #앞 뒤 바꿈

samsung.append('bio') #리스트에 요소 추가. 원본 바뀜
```



오브젝트가 행할 수 있는 행동들

형태 = 오브젝트.method()

원본 바뀌는 것 / 원본 안바뀌고 바로 출력 두 가지

numbers = [9, 5, 8, 1, 2]

sorted_numbers = numbers.sort()

sorted_numbers 에는 아무것도 저장되지 않음.  .sort() method 는 원본만 바꿈 



| str        | int   | list           | bool    | <=class  |
| ---------- | ----- | -------------- | ------- | -------- |
| `'string'` | `123` | `[a, 2 , 567]` | `False` | <=object |



## 6. Get lotto

1. pip install requests : 패키지 매니저에서 requests 모듈 설치

```python
import requests

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify=False)
lotto_data = response.json() #parsing 기존 str을 dict로 바꿈 (해석)

real_numbers = []

for key in lotto_data:                       #방법
    if 'drwtNo' in key:
        real_numbers.append(lotto_data[key])
        
for key, value in lotto_data.items():        #다른 방법
    if 'drwtNo' in key:
        real_numbers.append(value)

real_numbers.sort()
print(real_numbers)
```



json : 데이터의 표기법 Java script object notation



## 7. Weather

```python
from darksky import forecast

multicampus = forecast('c8f5585bd3f5ef841ee41709e398bd33', 37.501579, 127.039713)

print(multicampus['currently']['summary'])
print(multicampus['currently']['temperature'])
```

와!