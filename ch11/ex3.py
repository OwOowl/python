outFp = None
outStr = ''

outFp = open('C:/Temp/data2.txt', 'w')  # 'w' 파일 생성
while True:
    outStr = input('내용 입력 : ')
    if outStr != '':
        outFp.write(outStr + '\n')
    else :
        break

outFp.close()
print('---파일에 정상적으로 써졌음---')
