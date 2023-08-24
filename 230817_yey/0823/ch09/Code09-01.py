# 정적 크롤링 : 특정의 사이트의 내용(요소)을 가져오기
# 정적 크롤링(동적 크롤링 : 셀레니움(사용 빈도수 많음) , 
# 외부 API를 이용해서 수집)
# 스크래핑을 할 사이트를 정할 때, 영리 목적이 아니고, 누구나 자료를
# 봤을 떄, 크게 상관 없는 부분
import urllib.request

nateUrl = "https://www.nate.com"
# urlopen : 해당 사이트 주소의 html 관련 태그를 담는 임시 인스턴스
htmlObject = urllib.request.urlopen(nateUrl)
# htmlObject : 네이트 주소의 관련 태그들이 다 담겨져 있고.
# 
html = htmlObject.read()

print(html)