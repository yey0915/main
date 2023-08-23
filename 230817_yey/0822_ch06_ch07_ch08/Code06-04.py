# 파일 읽기
with open("C:/CookAnalysis/CSV/singer1.csv", "r") as inFp :
    # 파일 쓰기
    with open("C:/CookAnalysis/CSV/new_singer0822.csv", "w") as outFp:
        # inFp : csv 파일을 읽은 내용을 담은 임시 인스턴스
        header = inFp.readline()
        header = header.strip()
        header_list = header.split(',')
        # map 함수 : 첫번째 str 함수 : 문자열로 변경하는 함수
        # 두번째 인자 header_list 리스트의 요소를 하나씩 꺼내서 문자열화
        # 마지막 join 함수를 이용해서 콤마로 합치기
        header_str = ','.join(map(str, header_list))

        # csv에 쓰는 작업, outFp 인스턴스를 이용해서 쓰기 작업 수행
        # 첫행의 컬럼을 먼저 쓰기 작업
        outFp.write(header_str + '\n')
        # 2번째 행부터는 실제 데이터 값을 쓰는 작업
        # inFp : csv 파일의 내용을 담고 있는 인스턴스
        for inStr in inFp:
            # 한줄씩 읽고, 양쪽 공백 제거
            inStr = inStr.strip()
            # 콤마를 기준으로 나누기
            row_list = inStr.split(',')
            # row_list[-1] 리스트의 마지막 부분에 바꾸기
            row_list[-1] = row_list[-1].replace('.', '/')
            # row_list[-2] 리스트의 뒤에서 2번째, 값을 int로 정수화
            # 실수형으로 소수점 2번째 자리 확인 필요
            height_str = "{0:.2f}".format(int(row_list[-2]))
            # 키 값에 소수점으로 표기한 형식으로 재할당
            row_list[-2] = height_str
            row_str = ','.join(map(str, row_list))
            outFp.write(row_str + '\n')

print('Save. OK~')