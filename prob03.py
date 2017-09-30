# 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요
'''

실행 결과1

‘usr’, ‘local’, ‘bin’, ‘python’

실행 결과2

‘/usr/local/‘bin’ ‘python’


'''

s = '/usr/local/bin/python'

l = s.split('/')

l.pop(0)

# 첫번째 실행 결과

for i in range(0,len(l)):
    if i < len(l)-1:
         print('\''+l[i]+'\'', end=',')
    else:
         print('\''+l[i]+'\'')

t2 = s.split('/')

t2.pop(len(t2)-1)

s2='/'.join(t2)

# 두번째 실행 결과

print('\''+s2+'\'',end=' ')
print('\''+l[len(l)-1]+'\'')

''' 모범답안

s = '/usr/local/bin/python'
print(','.join(s[1:].split('/')))

# 디렉토리 경로명과 파일명을 분리하여 출력하세요.

print(','.join(s.rsplit('/', 1)))
=======

'''