import turtle as t

#실수형에서, 계산 결과 확인시 차이가 나는 부분
#우리는 10진수로 사용하지만, 컴퓨터에서는 모든 연산의 처리
#이진법으로 합니다.
a = 1.2
b = 1.4
c = 2.6

print("========메모리 위치값 확인하기========")
print(a+b == 2.6)
print(a+b)
print(f"a와 b의 메모리 주소값 비교 : a id b {a is b}")
print(f"a의 메모리 위치 주소값 id(a) : {id(a)}")
print(f"b의 메모리 위치 주소값 id(b) : {id(b)}")


print("======역순으로 문자열 출력===========")
cities = ['서울','부산','인천','대구']
str01 = 'abcdefgh'
print(str01[::-1])






