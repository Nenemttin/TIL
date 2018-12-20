import requests
import random

#define pick_lotto
def pick_lotto():
    numbers = random.sample(range(1, 46), 6)
    return numbers

#define get_lotto : 로또 홈페이지에서 api를 통해 n 회차 데이터를 받아오고 정제해서 번호 추출
def get_lotto(draw_no):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={}'.format(draw_no)
    lotto_data = requests.get(url).json() #parsing 기존 str을 dict로 바꿈 (해석)
    numbers = []
    for key, value in lotto_data.items():
        if 'drwtNo' in key:
            numbers.append(value)
    bonus = lotto_data['bnusNo']
    return {'numbers' : numbers, 'bonus' : bonus}

# define am_i_lucky

def am_i_lucky(pick, draw):
    #원래 내 코드
    # set_pick = set(pick)
    # draw_num = draw['numbers']
    # draw_bonus = draw['bonus']
    # inter_two = set_pick.intersection(set(draw_num))
    # match = len(inter_two)

    #어떤 자료형이 들어올 지 확신을 가지고 코드 짰음(draw에 dict) / 바꾼 코드(쌤 참고)
    match = len(set(pick) & set(draw['numbers']))

    if match == 6:
        return('축하합니다. 1등입니다!')

    elif match == 5 and draw['bonus'] in pick:
        return('축하합니다. 2등입니다!')

    elif match == 5:
        return('축하합니다. 3등입니다!')

    elif match == 4:
        return('축하합니다. 4등입니다!')

    elif match == 3:
        return('축하합니다. 5등입니다!')

    else:
        return('꽝')


result = am_i_lucky(pick_lotto(), get_lotto(837))



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

# if real_numbers == pick_numbers:
#     print('축하합니다. 1등입니다!')

# elif c == 5 and bonus_number in pick_numbers:
#     print('축하합니다. 2등입니다!')

# elif c == 5:
#     print('축하합니다. 3등입니다!')

# elif c == 4:
#     print('축하합니다. 4등입니다!')

# elif c == 3:
#     print('축하합니다. 5등입니다!')

# else:
#     print('꽝')