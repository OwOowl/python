
num1 = input('숫자1 --> ')
num2 = input('숫자2 --> ')

try:
    num1 = int(num1)
    num2 = int(num2)
    while True:
        res = num1 / num2
        print(res)

except ValueError:
    print('문자열은 숫자로 변환 안됨')
except ZeroDivisionError:
    print('0으로 나누면 안됨')
except KeyboardInterrupt:
    print('Ctrl + C를 눌렀군요')

