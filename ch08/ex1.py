ss = '파이썬짱'

# len(문자열) : 문자열의 길이를 나타내는 명령어
sslen = len(ss)

for i in range(0, sslen):
    print(ss[i] + '$', end='')

print()

inStr, outStr = ",", ","
count, i = 0, 0
inStr = input("문자열을 입력하세요")
count = len(inStr)

for i in range(0, count):
    outStr += inStr[count - (i + 1)]

print("내용을 거꾸로 출력 --> %s" % outStr)
