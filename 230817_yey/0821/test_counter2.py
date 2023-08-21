from collections import Counter

# 작은 따옴표 3개
# 그 안에 큰 따옴표 안에
# 필요한 텍스트 넣기
text = '''
    "Yesterday all my troubles seemed so far away

Now it looks as though they're here to stay

Oh, I believe in yesterday

Suddenly I'm not half the man I used to be

There's a shadow hanging over me

Oh, yesterday came suddenly.

Why she had to go I don't know,

she wouldn't say.

I said something wrong

now I long for yesterday.

Yesterday love was such an easy game to play

Now I need a place to hide away

Oh, I believe in yesterday

Why she had to go I don't know

she wouldn't say

I said something wrong

now I long for yesterday

Yesterday love was such an easy game to play

Now I need a place to hide away

Oh, I believe in yesterday"
'''.lower().split()

print(f"text 의 결과값 : {text}")
print(f"Counter 모듈이용 출력 : {Counter(text)}")
