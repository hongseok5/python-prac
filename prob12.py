# 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에 출력해보세요.
# 1부터 99까지만 실행하세요.

num = 1

for i in range(0,10,1):
    for j in range(1,11,1):
        if j % 3 == 0 and ( i==0 or i%3 != 0):
            print(num,'짝')
        elif j%3 == 0 and i%3 ==0:
            print(num,'짝짝')
        num += 1
# 파이썬은 논리연산을 and or not 으로 하고 $ | 은 바이너리 연산

''' 참고답안 

for n in range(1, 100):
    s = str(n)
    c = s.count('3') + s.count('6') + s.count('9')
    if c < 1:
        continue

    print("{0} {1}".format(s, '짝'*c))

'''