# ex7.py

sum, a, b = 0, 0, 0

while True :
    a = int(input("더 할 첫번째 수를 입력하세요 : "))
    b = int(input("더 할 두번째 수를 입력하세요 : "))
    sum = a + b
    print("%d + %d = %d" % (a, b, sum))