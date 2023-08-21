from collections import Counter

#gallahad 문자열 -> list 함수를 이용해서, 리스트 타입으로 변환
text = list("gallahad")
print(f"text 출력 : {text}")

c = Counter(text)
print(f"text 딕셔너리 형태로 바꿈(Counter()) : {c}")
print(f"text 딕셔너리 형태로 바꾼 아이템 갯수 출력 : {c['a']}")




