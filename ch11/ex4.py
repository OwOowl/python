
inFp, outFp = None, None
inStr = ''

inFp = open('C:/Temp/data1.txt', 'r', encoding='utf-8')
outFp = open('C:/Temp/data3.txt', 'w', encoding='utf-8')

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print('---복사 완료---')

