from collections import deque

s = set([1,2,3,4,5,2,3,4])
print(s)

print("==== 딕셔너리를 배워보자 ======================")
student_info = {20230821:'Sungchil', 20230822:'Jiyoung', 20230820:'JaeHong'}
print(f"댁셔너리의 키값으로 값을 가져오기 {student_info[20230820]}")
print(f"댁셔너리의 값을 가져오기 {student_info}")

print("=========Collection 모듈 테스트 ===============")
#line : 1의 import문 넣기
deque_list = deque()
for i in range(5) :
    deque_list.append(i)
print(f"deque_list의 출력 : {deque_list}")

# for i in range(5) :
#     deque_list.appendleft(i)
# print(f"deque_list appendldft 출력 : {deque_list}")
# print(deque_list)
# print(f"해당 deque의 요소의 메모리 위치 주소값 : id(deque_list[0]) : {id(deque_list[0])}")


# deque_list.rotate(2)
# print(f"test_deque_rotate 의 출력 : {deque_list}")
# print(f"해당 deque의 요소의 메모리 위치 주소값 : id(deque_list[2]) : {id(deque_list[2])}")

# test_deque_reverse = deque(reversed(deque_list))
# print(f"test_deque_reverse 의 출력 : {test_deque_reverse}")

deque_list.extend([5,6,7])
print(f"deque_list extends([5,6,7]) 출력 : {deque_list}")

deque_list.extendleft([8,9,10])
print(f"deque_list extendleft([8,9,10]) 출력 : {deque_list}")







