# 문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.

def reverse(s):

    return s[::-1]


s = input('입력>')
print(reverse(s))

# print() 안에 + 를 쓰게 되면 str + str 처럼 자료형이 같아야 한다, 콤마일 경우 상관 없음
# print() 안에 print(l)을 리턴하면 None이 리턴된다.