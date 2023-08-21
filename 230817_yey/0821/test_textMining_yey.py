from collections import defaultdict, OrderedDict

text = '''
    "다가오는 추석연휴 유럽·미주 등으로 장거리 '늦캉스'(늦은 휴가)를 떠날 계획이라면 서둘러야 한다.

10월 2일 하루 연차를 내면 6일까지 쉴 수 있는 '황금연휴'를 맞아 유럽 장거리 여행 상품 예약이 이미 가득차기 직전이기 때문이다. 코로나19 여파로 유럽여행에 대한 갈증이 쌓이면서 엔데믹을 맞아 추석 연휴를 활용하려는 사람들이 몰린 것으로 풀이된다. 여행·호텔 업계는 장거리 여행 수요 폭증을 주목하며 노선 증편하고 있다.


21일 교원투어 여행이지에 따르면 9월28일~10월3일 장거리 상품 비중이 전체의 49%에 달해 휴가철인 7말8초(7월28일~8월6일·46%) 대비 3%p 높게 나타났다.

유럽 중에서도 스페인, 이탈리아, 영국, 스위스 등 선호도가 높았다. 황금연휴 기간 서유럽 지역 좌석 소진율은 무려 89%에 달하는 것으로 집계됐다.

여행이지 관계자는 "스페인 경우 서유럽 전체와 맞먹는 항공 좌석을 확보하고 전세기 상품도 함께 선보이고 있다"며 "스페인 좌석 소진율은 80%를 돌파한 상태"라고 귀띔했다.

미국·캐나다 등 미주 지역 여행수요도 가파르게 증가했다. 캐나다 벤쿠버는 황금연휴 출발 좌석이 모두 소진됐고 뉴욕과 로스엔젤레스(LA) 좌석 소진율은 92%에 달했다.

하나투어(039130) 해외여행 수요 조사(9월27일~10월6일 출발)에서도 유럽 예약 비중이 눈에 띄게 증가했다. 해당기간 유럽 비중은 13.8%로 7말8초(9.3%) 대비 4.5%p 늘었다.

유럽 내 비중은 서유럽이 34.9%로 가장 높았고 동유럽(29.6%), 스페인(15.6%) 순이었다.

하나투어 관계자는 "추석연휴 유럽 지역 선예약률이 매우 높았는데 추석을 6개월 앞둔 시점에서 유럽 예약 비중은 전체의 45%를 차지할 정도였다"며 "장거리 여행은 일찌감치 예약하고 단거리 경우 여행일이 가까워지면 예약하는 현상이 이번 연휴에도 나타나고 있다"고 설명했다.

하나투어는 장거리 여행 수요 증가에 맞춰 크로아티아 자그레브 단독 전세기를 3회 운항하는 등 항공좌석 공급을 확대했다.

최근 메이저 여행사들끼리 좌석을 나눠 예약을 받는 '연합 전세기' 운영도 눈에 띄게 늘고 있다. 연합 전세기는 그리스, 스페인 바르셀로나, 캐나다 퀘벡, 이탈리아 베네치아 등 장거리 노선에 투입되고 있다.

여행 업계는 늦캉스족을 겨냥한 프로모션을 진행하고 있다.

노랑풍선은 8월은 '출발 임박 특가' 상품, 9월에는 '추석 황금연휴 출발 확정' 상품으로 월별 카테고리를 구분해 떠나기 좋은 상품을 최대 7% 할인해 판매한다.

야놀자는 '늦캉스도 야놀자해'라는 이름으로 '황금연휴 미리 예약 할인 쿠폰'을 발급하고 있다. 여기어때도 샌프란시스코 관광청과 손잡고 '올웨이즈 샌스란시스코' 프로모션을 진행 중이다.

글로벌 여행 플랫폼인 클룩은 31일까지 일본·동남아 주요 여행지 상품을 최대 50% 할인해주며 호텔스닷컴은 20일까지 국내외 숙박 시설 평균 20% 할인 행사를 열었다.

업계 관계자는 "성수기를 피해 늦캉스를 가려는 사람들이 눈에 띄게 늘었다"며 "앞으로는 단거리 여행지를 중심으로 추석 황금연휴 기간 예약률은 더 증가할 전망"이라고 했다."

'''.split()

word_count = defaultdict(lambda:0)

for word in text :
    word_count[word] += 1

test_OrderedDict = OrderedDict(sorted(word_count.items(), key=lambda t:t[1], reverse=True)).items()
print(f"test_OrderdDict 의 결과값 전체 : {test_OrderedDict}")

# print(f"test_OrderedDict 의 결과값 요소 i :{i}, v :{v}")
 

# for i, v in test_OrderdDict :
#     if v >= 3 :
#         print(f"test_OrderedDict 의 결과값 요소 i :{i}, v :{v}")

convlist = list(test_OrderedDict)

print(f"convlist 결과 값 ================ : {convlist}")

for i, v in convlist[:10] :
    print(f"test_OrderedDict 의 결과값 요소 i :{i}, v :{v}")