import requests

URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837'

got = requests.get(URL)

