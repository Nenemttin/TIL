import requests
import csv

boxoffice_date = [20181111, 20181118, 20181125, 20181202, 20181209, 20181216, 20181223, 20181230, 20190106, 20190113]

key = '149bb4a6a2cc08030fdf79d011560b29'
URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}'

collected_moviecd = []
collected_title = []
collected_audiacc = []
collected_date= []


for d in range(len(boxoffice_date)):
    data = requests.get(URL+f'&targetDt={boxoffice_date[d]}&weekGb=0').json()['boxOfficeResult']['weeklyBoxOfficeList']
    for i in range(10):
        collected_moviecd.append(data[i]['movieCd'])
        collected_title.append(data[i]['movieNm'])
        collected_audiacc.append(data[i]['audiAcc'])
        collected_date.append(boxoffice_date[d])

aggregate_data_dict = {}

for i in range(100):
    aggregate_data_dict[collected_moviecd[i]] = [collected_title[i], collected_audiacc[i], collected_date[i]]

# print(aggregate_data_dict)


my_boxoffice = []

for k, v in aggregate_data_dict.items():
    my_boxoffice.append([k]+v)
    
my_boxoffice
    
boxoffice = open('boxoffice.csv', 'w+', encoding='utf-8', newline='')

writer = csv.writer(boxoffice)

for data in my_boxoffice:
    writer.writerow(data)

boxoffice.close()
