''' 문제 13

a. 입력 받은 숫자가 홀수인 경우에는, 0 부터 입력 값까지 홀수의 합을 출력합니다.
- 예제 : 입력이 7 이면 16을 출력 ( 1 + 3 + 5 + 7 = 16 )
b. 입력 받은 숫자가 짝수인 경우에는, 0 부터 입력 값까지 짝수의 합을 출력합니다.
    - 예제 : 입력이 10 이면 30을 출력 ( 2 + 4 + 6 + 8 + 10 = 30 )

'''

number = input('숫자를 입력하세요:')
if number.isdigit() == False:
    print('정수를 입력하세요')
else:
    number = int(number)
    sum = 0
    if number % 2 == 0:

        for i in range(0,number+1,2):
            sum += i


    else:
        for i in range(1,number+1,2):
            sum += i
    print(sum)

''' 참고답안 

number = input('숫자를 입력하세요: ')
if number.isdigit() is False:
    print('숫자를 입력하세요')
    sys.exit(0)

number = int(number)
iseven = number & 0x0001 == 0

s = 0
for n in range(number+1):
    if iseven and n & 0x0001 == 0:
        s += n
    elif not iseven and n & 0x0001 == 1:
        s += n

print("결과 값 : {0}".format(s))

'''