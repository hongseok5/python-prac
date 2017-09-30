# 주어진 if 문을 dict를 사용하도록 수정하세요.

"""
if menu == '오뎅':
    price = 300
elif menu == '순대':
    price = 400
elif menu == '만두':
    price = 500
else:
    price = 0
"""

d = {'오뎅':300,'순대':400,'만두':500}
menu = input('메뉴: ')

if menu in d:

    print(menu,'의 가격은',d[menu],'원 입니다')

else:
    print(menu+'는 팔지 않습니다')