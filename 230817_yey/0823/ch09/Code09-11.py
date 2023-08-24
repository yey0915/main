import bs4
import urllib.request

nateUrl = "https://news.nate.com"
htmlObject = urllib.request.urlopen(nateUrl)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

# div -> 속성 : class, 값 : snbArea
tag = bsObject.find('div', {'class':'snbArea'})

print('## 네이트 뉴스의 메뉴 목록 ##')
# div -> 속성 값 : class, 값 : snbArea의 값을 리스트에 저장
li_list = tag.findAll('li')
print(f"li_List 의 값 목록 : {li_list}")
for li in li_list :
    print(li.text, end='  ' )
    a_tag = li.find("a")
    print(f"li 태그의 값 : {a_tag}")
    a_tag_href = a_tag.find("href")
    print(f"a.href 태그의 값 : {a_tag_href}")
    # print(li['href'].text, end='  ' )