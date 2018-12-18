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


# my_numbers, real_numbers, bonus_number
# 1등 : real_numbers == pick_numbers
if real_numbers == pick_numbers:
    print('축하합니다. 1등입니다.')
# 2등 : real_numbers & pick_numbers 가 5개가 같고, pick_numbers의 나머지 하나가 bonus_number
elif 
    print('축하합니다. 2등입니다.')
# 3등 : real_numbers & pick_numbers 가 5개가 같다
elif
    print('축하합니다. 3등입니다.')
# 4등 : real_numbers & pick_numbers 가 4개가 같다
elif
    print('축하합니다. 4등입니다.')
# 5등 : real_numbers & pick_numbers 가 3개가 같다
elif
    for number in pick_numbers:
        if number in real_numbers:
            

    print('축하합니다. 5등입니다.')
# 꽝
else:
    print('꽝')

