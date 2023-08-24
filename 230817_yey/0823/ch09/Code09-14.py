import bs4
import urllib.request

# yes24 특정, 도서 정보를 가져오기, 콘솔 출력, 특정 한페이지만

## 함수 선언부
def getBookInfo(book_tag) :
    names = book_tag.find("div", {"class": "goods_name"})
    bookName = names.find("a").text
    auths = book_tag.find("span", {"class": "goods_auth"})
    bookAuth = auths.find("a").text
    bookPub = book_tag.find("span", {"class": "goods_pub"}).text
    bookDate = book_tag.find("span", {"class": "goods_date"}).text
    bookPrice = book_tag.find("em", {"class": "yes_b"}).text
    return [bookName, bookAuth, bookPub, bookDate, bookPrice]

## 전역 변수부
# 해당 사이트의 하위 주소 부분 반드시 조사.
bookUrl = "http://www.yes24.com/24/Category/Display/001001046001?ParamSortTp=05&PageNumber=1"

## 메인 코드부
# 가독성
htmlObject = urllib.request.urlopen(bookUrl)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

# 태그의 트리 구조 조사, 정보 접근
# ul > .clearfix -> div.goods_info 의 모든 값을 리스트에 담기
tag = bsObject.find('ul', {'class': 'clearfix'})
all_books = tag.findAll('div', {'class': 'goods_info'})
# print(f"yes24 tag 자료 ============== : {all_books}")

for book in all_books :
    print(getBookInfo(book))