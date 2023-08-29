import bs4
import urllib.request

# # 원하는 정보가 담긴 table 가지고 왔음 - DB에 저장하기(과제~!!!!!!!!!)
# nateUrl = "http://api.nongsaro.go.kr/sample/rest/garden/garden.jsp"
# htmlObject = urllib.request.urlopen(nateUrl)
# webPage = htmlObject.read()
# bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

# tag_list = bsObject.findAll('table')
# print("================================= 마지막 table 값")
# print(tag_list[-1])



nateUrl = "https://www.kaggle.com/datasets?tags=13302-Classification#site-content"
htmlObject = urllib.request.urlopen(nateUrl)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

tag_list = bsObject.find('div', {"id":"site-container"})
print("=================================== 캐글 데이타 셋")
print(tag_list)


# tag_list = bsObject.find('div', {"id":"site-container"})
# print("=================================== 캐글 데이타 셋")
# print(tag_list)
# tag_ul = tag_list.find("div", {"id":"rmwcPortal"})
# print(tag_ul)






