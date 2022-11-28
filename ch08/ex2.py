# ss = input("입력 문자열 ==> ")
# print("출력 문자열 ==> ", end="")
#
# if ss.startswith("(") == False:
#     print("(", end="")
#
# print(ss, end="")
#
# if ss.endswith(")") == False:
#     print(")", end="")

print()

inStr = '   한글 Python 프로그래밍     '
outStr = ''  # inStr에 공백문자열 제거하고 리턴

for i in range(0, len(inStr)):
    if inStr[i] != ' ':
        outStr += inStr[i]


print('원래 문자열 ==> ' + '[' + inStr + ']')
print('공백 삭제 문자열 ==> ' + '[' + outStr + ']')

inStr = 'Live as if you will die today'

# replace('문자열1', '문자열2') : 문자열1을 문자열2로 변환
print(inStr.replace('i', '$'))



