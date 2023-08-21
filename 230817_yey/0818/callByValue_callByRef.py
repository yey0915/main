#Call By Value

def f(x):
    global z
    z = 10
    y=x
    x=5
    return y*y
    #global x, 이미 전역으로 사용된 변수를, 함수 내부에서 전역으로 선언 불가


#전역
x = 3
print(f(x))
print(x)

print("========call by reference========================================")
#call by Reference
def spam(eggs):
    eggs.append(1)
    # eggs 효력 범위, 시작 끝으로 생명주기를 다함
    #[2,3] 리스트이고 이것은 다른 인스턴스
    eggs = [2,3]

ham = [0]
spam(ham)
print(ham)
