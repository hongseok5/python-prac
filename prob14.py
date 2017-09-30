import sys
import random

n = random.randrange(100) + 1
min = 1
max = 100

print(1,'-',100)
number = input("숫자를 맞춰보세요")
if number.isdigit() == True:
    number = int(number)

    while True:

        if n > number:
            min = number
            print(min, '-', max)
            number = int(input('더 높게'))

            continue
        elif n < number:
            max = number
            print(min, '-', max)
            number = int(input('더 낮게'))

            continue
        else:
            print('맞았습니다')

            answer = input('다시 하시겠습니까(y/n)>>')
            if answer == 'y':
                print('ctrl+shift+f10')
            elif answer == 'n':
                print('수고하셨습니다')
            else:
                print('y or n 로 입력해주세요')


else:
    print('숫자를 입력하시오')