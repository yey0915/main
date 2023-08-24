import bs4

webPage = open('C:/CookAnalysis/HTML/Sample02.html', 'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')    #가독성 있게 사이트 내용 변환

tag_div = bsObject.find('div')
print(tag_div)