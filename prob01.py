# 홀수,짝수 구분하는 코드



number = input('수를 입력하시오:')

if number.isdigit() is False:
    print('정수를 입력하시오')


else:
    number = int(number)
    if number % 2 == 0:
        print('짝수입니다')

    else:
        print('홀수입니다.')

