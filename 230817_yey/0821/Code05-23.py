inFp, outFp = None, None 
inStr = ""

inFp = open("C:/Windows/write.exe", "rb")
outFp = open("C:/Temp/write.exe", "wb")

# 계속 파일의 내용을 없을 떄까지 계속 쓰기
while True :
    # 읽는 인스턴스에서 1바이트씩 읽어서
    inStr = inFp.read(1)
    # 없으면 반복문 빠져나가고
    if not inStr :
        break
    # 그렇지 않다면, 내용이 있다면, 바이너리로 쓰기 작업.
    outFp.write(inStr)

inFp.close()
outFp.close()
print("--- 이진 파일이 정상적으로 복사되었음 ---")
