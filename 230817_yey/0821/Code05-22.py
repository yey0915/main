inFp, outFp = None, None 
inStr = ""

inFp = open("C:/Windows/win.ini", "r")  # 읽는 객체
outFp = open("C:/Temp/data3.txt", "w")  # 쓰는 객체

inList = inFp.readlines()
for inStr in inList :
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("--- 파일이 정상적으로 복사되었음 ---")
