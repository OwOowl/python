'''
filename : ex3.py
author : minho
date : 2022.11.28
'''

ss = input('날짜(연/월/일) 입력 ==> ')

# split() : 지정한 문자열 기준으로 문자열 나누기
ssList = ss.split('/')
print("입력한 날짜의 10년 후 ==> ", end="")
print(str(int(ssList[0]) + 10) + "년", end="")
print(ssList[1] + '월', end='')
print(ssList[2] + '일', end='')
