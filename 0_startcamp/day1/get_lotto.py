import requests

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
print(real_numbers)