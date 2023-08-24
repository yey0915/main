import csv
import time
import datetime
import bs4
import urllib.request

# 날씨의 정보를 크롤링 해서 -> 실제 csv 파일에 쓰는 예제

csvName =  'c:/CookAnalysis/CSV/sokcho_weather_0823.csv'
with open(csvName, 'w', newline='') as csvFp:
    csvWriter = csv.writer(csvFp)
    # 첫번째 헤더 부분, 컬럼
    csvWriter.writerow(['연월일', '시분초', '온도', '습도', '강수량', '풍향'])

nateUrl = "https://news.nate.com/weather?areaCode=11D20401"
while True :
    # 가독성
    htmlObject = urllib.request.urlopen(nateUrl)
    webPage = htmlObject.read()
    bsObject = bs4.BeautifulSoup(webPage, 'html.parser')


    # 가져올 정보의 태그 트리. 
    # div : .right_today -> 
    tag = bsObject.find('div', {'class': 'right_today'})
    # div : .right_today -> p : .celsius, text값 가져오기
    temper = tag.find('p', {'class': 'celsius'}).text
    # div : .right_today -> p : .humidity, text값 가져오기
    humi = tag.find('p', {'class': 'humidity'}).text
    rain = tag.find('p', {'class': 'rainfall'}).text
    wind = tag.find('p', {'class': 'wind'}).text

    # 사용자 정의 날짜, 시간
    now = datetime.datetime.now()
    yymmdd = now.strftime('%Y-%m-%d')
    hhmmss = now.strftime('%H:%M:%S')

    weather_list = [yymmdd, hhmmss, temper, humi, rain, wind]
    with open(csvName, 'a', newline='') as csvFp:
        csvWriter = csv.writer(csvFp)
        csvWriter.writerow(weather_list)
        print(weather_list)

    time.sleep(10)
