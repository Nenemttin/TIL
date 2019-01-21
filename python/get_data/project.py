import requests
import csv
from time import sleep
import urllib.request
import os

boxoffice_date = [20181111, 20181118, 20181125, 20181202, 20181209, 20181216, 20181223, 20181230, 20190106, 20190113]

key = '149bb4a6a2cc08030fdf79d011560b29'
URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}'

collected_moviecd = []
collected_title = []
collected_audiacc = []
collected_date= []


for d in range(len(boxoffice_date)):
    data = requests.get(URL+f'&targetDt={boxoffice_date[d]}&weekGb=0').json()['boxOfficeResult']['weeklyBoxOfficeList']
    for i in range(len(boxoffice_date)):
        collected_moviecd.append(data[i]['movieCd'])
        collected_title.append(data[i]['movieNm'])
        collected_audiacc.append(data[i]['audiAcc'])
        collected_date.append(boxoffice_date[d])


aggregate_data_dict = {}

for i in range(100):
    aggregate_data_dict[collected_moviecd[i]] = [collected_title[i], collected_audiacc[i], collected_date[i]]


my_boxoffice = []

for k, v in aggregate_data_dict.items():
    my_boxoffice.append([k]+v)
    
my_boxoffice
    
boxoffice = open('boxoffice.csv', 'w+', encoding='utf-8', newline='')

writer = csv.writer(boxoffice)

for data in my_boxoffice:
    writer.writerow(data)

boxoffice.close()

# movie detail

URL_DETAIL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd='

moviecds = []

for i in my_boxoffice:
    moviecds.append(i[0])

movienms = []
movienmens = []
movienmogs = []
opendts = []
showtms = []
genres = []
directorsall = []
watchgradenms = []
actors = []

data_detail = requests.get(URL_DETAIL+f'{20184574}').json()['movieInfoResult']['movieInfo']

for de in moviecds:
    data_detail = requests.get(URL_DETAIL+f'{de}').json()['movieInfoResult']['movieInfo']
    movienms.append(data_detail['movieNm'])
    movienmens.append(data_detail['movieNmEn'])
    movienmogs.append(data_detail['movieNmOg'])
    opendts.append(data_detail['openDt'])
    showtms.append(data_detail['showTm'])
    genres.append(data_detail['genres'][0]['genreNm'])
    directorsall.append(data_detail['directors'][0]['peopleNm'])
    watchgradenms.append(data_detail['audits'][0]['watchGradeNm'])
    if len(data_detail['actors']) >= 3:
        actors.append([data_detail['actors'][0]['peopleNm'], data_detail['actors'][1]['peopleNm'], data_detail['actors'][2]['peopleNm']])
    elif len(data_detail['actors']) == 2:
        actors.append([data_detail['actors'][0]['peopleNm'], data_detail['actors'][1]['peopleNm']])
    elif len(data_detail['actors']) == 1:
        actors.append([data_detail['actors'][0]['peopleNm']])
    elif len(data_detail['actors']) == 0:
        actors.append([])

aggregate_movie_detail_data_dict = {}

for i in range(len(moviecds)):
    aggregate_movie_detail_data_dict[moviecds[i]] = [movienms[i], movienmens[i], movienmogs[i], opendts[i], showtms[i], genres[i], directorsall[i], watchgradenms[i]] 


my_movie_detail = []

for k, v in aggregate_movie_detail_data_dict.items():
    my_movie_detail.append([k]+v)

for i in range(len(moviecds)):
    my_movie_detail[i] += actors[i]


movie = open('movie.csv', 'w+', encoding='utf-8', newline='')

writer = csv.writer(movie)

for data in my_movie_detail:
    writer.writerow(data)

movie.close()

# movie_naver

naver_uri = 'https://openapi.naver.com/v1/search/movie.json?query='

client_id = 'baxnvG2Y6JHS3u7ahepV'
client_secret = 'fg17WWeXIJ'
headers = { 
    'X-Naver-Client-Id': client_id,
    'X-Naver-Client-Secret': client_secret
}

result = []

for movie in movienms:
    sleep(0.5)
    data_set = requests.get(naver_uri + movie, headers=headers).json()
    movie_info = {}
    movie_info['movie_info'] = [data_set['items'][0]['title'], data_set['items'][0]['link'], data_set['items'][0]['image'], data_set['items'][0]['userRating']]
    result.append(movie_info)


aggregate_naver_movie = []

for naver_dict in result:
    for k, v in naver_dict.items():
        aggregate_naver_movie.append(v)
        
for title in aggregate_naver_movie:
    title[0] = title[0].replace('<b>', '')
    title[0] = title[0].replace('</b>', '')


for i in range(len(moviecds)):
    aggregate_naver_movie[i].insert(0, moviecds[i])


movie_naver = open('movie_naver.csv', 'w+', encoding='utf-8', newline='')

writer = csv.writer(movie_naver)

for data in aggregate_naver_movie:
    writer.writerow(data)

movie_naver.close()

#images download

# file path and file name to download
outpath = "C:\\Users\\student\\PARK-BYEONG-JUN\\Projects\\01_python\\images\\"

# download
for i in range(len(moviecds)):
    sleep(0.5)
    urllib.request.urlretrieve(aggregate_naver_movie[i][3], outpath+aggregate_naver_movie[i][0]+'.jpeg')
