# 1. 평균을 구하시오
my_score = [79, 84, 66, 93]
my_average = sum(my_score) / len(my_score)
print(my_average)






your_score = {
    '수학': 87,
    '국어': 83,
    '영어': 76,
    '도덕': 100
}

your_average = sum(your_score.values()) / len(your_score)
print(your_average)

cities_temp = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -5, 10],
    '구미': [2, -2, 9]
}

# seoul_average = sum(cities_temp['서울']) / len(cities_temp['서울'])
# daejeon_average = sum(cities_temp['대전']) / len(cities_temp['대전'])
# gwangjoo_average = sum(cities_temp['광주']) / len(cities_temp['광주'])
# goomi_average = sum(cities_temp['구미']) / len(cities_temp['구미'])

# print('서울:', round(seoul_average, 2))
# print('대전:', round(daejeon_average, 2))
# print('광주:', round(gwangjoo_average, 2))
# print('구미:', round(goomi_average, 2))



# 3: 도시별 온도 평균
for city, temperatures in cities_temp.items():
    avg_temperature = round(sum(temperatures) / len(temperatures), 2)
    print('{0}: {1}'.format(city, avg_temperature))

# 4: 도시 중에 최근 3일간 가장 추웠던 곳, 가장 더웠던 곳
# Hottest : ??, Coldest: ?? 
temp_summary = []

for city, temp in cities_temp.items():
    temp_summary += temp

max_temp = max(temp_summary)
min_temp = min(temp_summary)

hottest = []
coldest = []
for city, temp in cities_temp.items():
    if max_temp in temp:
        hottest.append(city)
    if min_temp in temp:
        coldest.append(city)

print(hottest, coldest)

#all_temp 모든 기온을 모은다

#all_temp에서 highest / lowest를 찾는다

#cities_temp 에서 highest / lowest가 속한 도시를 찾는다.

