# 이중 리스트에서, 각 요소의 메모리 위치 주소값 확인
a = [[1,2],[3,4]] # 2 X 2 배열
print(f"a 리스트의 a[0]의 메모리 위치 주소값 확인 : {id(a[0])}")
print(f"a 리스트의 a[0]의 메모리 위치 주소값 확인 : {id(a[1])}")
print(f"a 리스트의 a[0]의 메모리 위치 주소값 확인 : {id(a[0][0])}")

