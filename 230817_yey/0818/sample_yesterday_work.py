f = open("./0818/yesterday_utf.txt", 'r', encoding='utf-8')
yesterday_lyric = f.readlines()
print(f"파일 읽어 오기 : {yesterday_lyric}")
f.close()

contents = ""
for line in yesterday_lyric:
    contents = contents + line.strip() + "\n"

    print(contents)
count = contents.upper().count("YESTERDAY")

print(f"가사중에 yessterday를 대문자로 변환 후 갯수 찾은 결과 : {count}")




