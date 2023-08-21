from collections import defaultdict, OrderedDict
# defaultdict : 값이 없는 경우 지정된 디폴트 값으로 대체.

text = '''
    "Yesterday all my troubles seemed so far away

Now it looks as though they're here to stay

Oh, I believe in yesterday

Suddenly I'm not half the man I used to be

There's a shadow hanging over me

Oh, yesterday came suddenly.

Why she had to go I don't know,

she wouldn't say.

I said something wrong

now I long for yesterday.

Yesterday love was such an easy game to play

Now I need a place to hide away

Oh, I believe in yesterday

Why she had to go I don't know

she wouldn't say

I said something wrong

now I long for yesterday

Yesterday love was such an easy game to play

Now I need a place to hide away

Oh, I believe in yesterday"
'''.upper().split()

#defaultdict -> 값이 없으면 기본값을 0으로 지정
# lamda 매개변수 : 수행하려는 문장(리턴)
word_count = defaultdict(lambda:0)

for word in text :
    word_count[word] += 1
    
# OrderedDict 이용해서 정렬
# OrderedDict(매개변수1(정렬된 딕셔너리)).items -> 키, 값을 둘다 가져오는 구조.
# sorted(매개변수1(집계된 딕셔너리 키와 값), 매개변수2(정렬기준 : 람다식),
#       매개변수3(기본 오름차순, reverse=True 내림차순))
# lamda t:t[1] -> t : 매개변수(튜플 형식), t[1] : 결과값 (value)
test_OrderdDict = OrderedDict(sorted(word_count.items(), key=lambda t:t[1], reverse=True)).items()
print(f"test_OrderdDict 의 결과값 전체 : {test_OrderdDict}")


# cnt = 0
# tempStr = ''
# for i, v in test_OrderdDict :    
#     if cnt <= 5 :
#         print(f"test_OrderedDict 의 결과값 요소 i :{i}, v :{v}")
#         tempStr = "{v}"
#     else : break
#     cnt = cnt + 1
#     print(f"cnt 값 : {cnt}")

#top10 뽑아내기
convertedList = list(test_OrderdDict)
print(f"top 10 결과값 : {test_OrderdDict}")
for i, v in convertedList[:10] :
    print(f"top 10 결과값 : {i}, v : {v}")




