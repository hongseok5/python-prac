# 다음과 같은 테스트에서 모든 태그를 제외한 텍스트만 출력하세요.

s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
            To connect to the most powerful tolls int the world.
        </p>
    </body>
</html>"""

isTag = False
result = ''

for c in s:
    if c =='<':
        isTag=True
        result += ' '
    elif c == '>':
        isTag=False
        result += ' '
    elif c == '\n':
        result += '\n'
    elif isTag == False:
        result += c
    else:
        result += ' '
        # 마지막에 else가 없어도 비슷한 결과가 나오지만 Here 의 위치가 다름
print(result)



'''  모범답안 

idxbegin = 0

while True:
    idxbegin = s.find('<', idxbegin)
    if idxbegin == -1:
        break
    idxend = s.find('>')
    if idxend != -1:
        s = s[:idxbegin] + s[idxend+1:]
    else:
        idxend += 1

'''