# 3의 배수를 확인하는 코드


number = input('수를 입력하시오')
if number.isdigit() == False:
    print('정수를 입력하시오')
else:
    number = int(number)
    if number % 3 == 0:
        print('3의 배수입니다')
    else:
        print('3의 배수가 아닙니다')


