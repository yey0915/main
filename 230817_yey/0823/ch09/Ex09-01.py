import time
import bs4
import urllib.request

# 네이트 실시간 뉴스 정보 -> 콘솔에 출력
# 코드를 수정해서 MySql 자동으로 저장
nateUrl = "https://news.nate.com/recent?mid=n0100"
# while True :
    # 가독성
htmlObject = urllib.request.urlopen(nateUrl)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

# div.mlt01 -> 정보가 20개
# tag_list<mlt01> -> 기사 하나의 데이터 형태
tag_list = bsObject.findAll('div', {'class': 'mlt01'})
print("========================================")
print(tag_list)
print("========================================")
    # print('###### 실시간 뉴스 속보 #######')
    # # 숫자를 표현하기 위해 붙인것
    # num = 1
    # for tag in tag_list :
    #     # 각 기사에서, 특정 정보를 추출하는 작업
    #     subject = tag.find('h2', {'class': 'tit'}).text
    #     link = tag.find('a', {'class': 'lt1'})['href']
    #     pressAndDate = tag.find('span', {'class': 'medium'}).text
    #     pressAndDate.replace('\t',' ')
    #     pressAndDate.replace('\n', '')

    #     if len(pressAndDate.split()) == 3 :
    #         press, pDate, pTime = pressAndDate.split()
    #     elif len(pressAndDate.split()) == 4 :
    #         press1,press2, pDate, pTime = pressAndDate.split()
    #         press = press1+press2
    #     else :
    #         continue

    #     print('(' , num, ')', subject)
    #     print('\t https:'+link, press, pDate, pTime)
    #     num += 1

    # time.sleep(60)