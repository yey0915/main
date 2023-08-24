import bs4

webPage = open('C:/CookAnalysis/HTML/Sample02.html', 'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

# ul 태그 찾아 출력하기
tag_ul= bsObject.find('ul')
print(tag_ul)
print()

tag_li= bsObject.find('li')
print(tag_li)
print()

# 이전은 단수의 태그를 찾았다면 findAll은 복수개의 태그를 찾는다.
tag_li_all= bsObject.findAll('li')
print(f"tag_li_all를 찾는다 : {tag_li_all}")