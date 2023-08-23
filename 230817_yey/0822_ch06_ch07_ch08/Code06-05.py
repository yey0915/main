# csv 파일 읽기, 쓰기, 특정 컬럼에 대해서 작업.
with open("C:/CookAnalysis/CSV/singer1.csv", "r") as inFp :
    with open("C:/CookAnalysis/CSV/new_singer2_0822_height.csv", "w") as outFp:
        header = inFp.readline()
        header = header.strip()
        header_list= header.split(',')
        # 특정 컬럼 인덱스 출력
        idx1 = header_list.index('아이디')
        idx2 = header_list.index('이름')
        idx3 = header_list.index('평균 키')
        # 특정 컬럼의 값을 추출해서 리스트화
        header_list = [header_list[idx1], header_list[idx2], header_list[idx3]]
        # 리스트 워너소를 하나씩 꺼내서 문자열로 변환 후 콤마를 기준으로 합치기
        header_str = ','.join(map(str, header_list))
        # csv 쓰기 인스턴스 outFp, 먼저 1행 컬럼 부분을 쓰기
        outFp.write(header_str + '\n')
        for inStr in inFp:
            inStr = inStr.strip()
            row_list = inStr.split(',')
            if int(row_list[idx3]) >= 165 :
                # 평균키 165 이상이면 쓴다
                # 
                row_list = [row_list[idx1], row_list[idx2], row_list[idx3]]
                row_str = ','.join(map(str, row_list))
                outFp.write(row_str + '\n')

print('Save. OK~')