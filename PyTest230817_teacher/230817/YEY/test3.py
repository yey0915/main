print("=========== 십진수를 이진수로 변환하기 ===================================")

decimal = 10
result = ''
while(decimal > 0):
    remainder = decimal % 2
    print(f"{decimal}/2 의 나머지 {remainder}")
    decimal = decimal // 2
    result = str(remainder) + result
    print(f"10의 이진수를 만들기 {result}")
print(result)

print("============ 문자열 역순으로 변환하기 =================================")
str = "abcdefghi"
print(f"문자열 : {str}")
print(str[len(str):0:-1])


print("=========== 구구단을 하자 ==========================================")
for i in range(1, 10) :
    for j in range(1, 10) : 
        print(f"{i} * {j} = {j*i}")