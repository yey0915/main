import bs4

webPage = open('C:/CookAnalysis/HTML/Sample03.html', 'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

# 각 태그의 속성까지 포함해서 검색
tag = bsObject.find('div', {'id':'myId1'})
print(tag)

tag = bsObject.find('div', {'class':'myClass1'})
print(tag)

# 복수로 찾을 시 리스트를 findAll로 찾아서 출력
tag = bsObject.findAll('div', {'class':'myClass1'})
print(tag)