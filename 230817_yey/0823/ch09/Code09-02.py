import urllib.request
import bs4

nateUrl = "https://www.nate.com"
htmlObject = urllib.request.urlopen(nateUrl)
# 위의 코드는 정리가 덜 된 태그 집합
# 아래 코드는 bs4 -> BeautifulSoup 클래스를 이용해서, 가독성 있게 변환
bsObject = bs4.BeautifulSoup(htmlObject, 'html.parser')

print(bsObject)