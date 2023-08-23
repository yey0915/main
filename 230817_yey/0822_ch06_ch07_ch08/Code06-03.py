# 함수, 매개변수(리스트), 반환값 없음
def printList(pList) :
    for data in pList :
        print(data, end='\t')
    print()

# 자동 닫는 버전으로, 인스턴스 생성(csv 파일 내용을 읽는 임시 저장 내용(메모리))
with open("C:/CookAnalysis/CSV/singer1.csv", "r") as inFp :
    # 1 행 : 해당 칼럼
    header = inFp.readline()
    # 헤더 부분의 양쪽 공백 제거
    header = header.strip()
    # 헤더의 내용을 split(',') 콤마를 기준으로 나누는 작업
    # 1번째 : 컬럼 여기는 두번째 행은 실제 데이터
    header_list = header.split(',')
    printList(header_list)
    for inStr in inFp:
        inStr = inStr.strip()   # 공백 제거
        row_list = inStr.split(',')
        printList(row_list)