import requests
import random

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify=False)
lotto_data = response.json() #parsing 기존 str을 dict로 바꿈 (해석)

real_numbers = []

# for key in lotto_data:
#     if 'drwtNo' in key:
#         real_numbers.append(lotto_data[key])

for key, value in lotto_data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)

real_numbers.sort()
bonus_number = lotto_data['bnusNo']

numbers = list(range(1, 46))

pick_numbers = random.sample(numbers, 6)
pick_numbers.sort()

print(real_numbers)
print(pick_numbers)

a = set(real_numbers)
b = set(pick_numbers)
c = len(a.intersection(b))

if real_numbers == pick_numbers:
    print('축하합니다. 1등입니다!')

elif c == 5 and bonus_number in pick_numbers:
    print('축하합니다. 2등입니다!')

elif c == 5:
    print('축하합니다. 3등입니다!')

elif c == 4:
    print('축하합니다. 4등입니다!')

elif c == 3:
    print('축하합니다. 5등입니다!')

else:
    print('꽝')