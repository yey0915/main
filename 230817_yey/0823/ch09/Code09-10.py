import bs4
import urllib.request

# 찾을 때, 웹 브라우저의 검사(f12 개발자 도구, element 요소탭에서)
# Ctrl + Shift + c, 웹 화면에 마우스 커서를 올려보면 해당 요소의 태그 
# 및 정보를 알 수  있음

nateUrl = "https://www.nate.com"
htmlObject = urllib.request.urlopen(nateUrl)
webPage = htmlObject.read()
# 가독성 있게 변환
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

# div 태그중 id의 값이 NateBi인 값 :네이트 로고
tag = bsObject.find('div', {'id':'NateBi'})
print('==============================')
print(tag , '\n')
# div -> id 속성 값 :NateBi : tag 담았고 -> 하위의 a 태그 찾기 : a_tag에 할당
a_tag = tag.find("a")
print('==============================')
print(a_tag , '\n')

# div -> id 속성 값 :NateBi : tag 담았고 -> 하위의 a 태그 찾기 : a_tag에 할당
# 이어서 속성 href 의 값만 추출
href = a_tag['href']
print('==============================')
print( href , '\n')
print('==============================')

# 해당 태그의 텍스트만 추출
text = a_tag.text
print(text)