import bs4

webPage = open('C:/CookAnalysis/HTML/Sample03.html', 'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
print("======= bsObject ==============================================\n")
print(bsObject)

# 중요!!! : 활용도 높음
a_list = bsObject.findAll('a')

for aTag in a_list :
    print( aTag['href'] )
