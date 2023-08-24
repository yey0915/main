import bs4

# 실제 사이트에 접근하기 전에
# 임시 html에서, 각 태그별 접근 연습
webPage = open('C:/CookAnalysis/HTML/Sample02.html', 'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

print(bsObject)

# 각 태그의 속성까지 포함해서 검색
tag = bsObject.find('div', {'id':'myId1'})
print(tag)

tag = bsObject.find('div', {'class':'myClass1'})
print(tag)

# 복수로 찾을 시 리스트를 findAll로 찾아서 출력
tag = bsObject.findAll('div', {'class':'myClass1'})
print(tag)

