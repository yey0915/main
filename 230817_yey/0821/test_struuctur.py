# 자료 구조별 slice 해보기
word = "Input a word:"
print(f"word 의 자료 형태 : {word}")

# 리스트 형태로 바꿈
wordList = list(word)
print(f"list 형태의 word : {wordList}")
print(f"list 형태의 자료의 slicing : {wordList[:]}")

# 튜플
t = tuple(wordList)
print(f"튜플로 바꾼 word 리스트 자료의 형태 : {t}")
print(f"튜플로 바꾼 word의 slicing : {t[:]}")


# 세트
s = set(word)
s02 = ([[1,2], [2,3], [1,3]])
print(f"word의 세트 자료 형태 : {s}")
print(f"word의 세트 자료 형태 : {s02}")

#딕셔너리
student_info = {20220123 : 'Sh', 20220918: 'Jiy', 20321234: 'JH'}
print(f"딕셔너리 student_info 의 자료 형태 : {student_info}")
si = list(student_info)
print(f"student_info 의 list 자료 형태로 변환 : {si}")
print(f"딕셔너리 student_info의 slicing : {si[:]}")


count_code = {"US" : 1, "KR" : 82, "CHINA" : 86, "JP" : 81, "GRICE":30, "SWISS" : 44}
print(f"딕셔너리 출력 연습 값 values : {count_code.values()}")
print(f"딕셔너리 출력 연습 keys : {count_code.keys()}")
print(f"딕셔너리 출력 리스트 변환 : {list(count_code.values())}")
cntList = list(count_code.values())
print(f"딕셔너리 출력 리스트 변환 : {cntList[:]}")




