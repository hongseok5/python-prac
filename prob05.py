# 다음 문자열을 모든 대문자를 소문자로 변환하고, 문자 ',', '.','\n'를 없앤 후에 각 단어를 순서대로 출력하세요.
# 대문자를 소문자로 바꾸고, 마침표,쉼표,개행 없애고, 중복 없이 각 단어를 순서대로 출력.
# s.upper(), s.lower()

s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

# 모든 문자를 소문자로
s=s.upper()
s=s.lower()

# 모든 개행, 마침표, 쉼표를 제거

s=s.replace('.','')
s=s.replace(',','')
s=s.replace('\n','')

l = s.split(' ')
l2 = list(set(l))
l2.sort()

# 첫번째 출력
for i in l2:
    print(i)

# 두번째 출력
print("="*10,'단어 개수',"="*10)
for j in l:

    print('{0}:{1}'.format(j,s.count(j)))
    #l 은 리스트이고 s는 문자열인데 l로 for문 돌리면서 s안에 리스트 요소를 카운트 하는게 가능함



