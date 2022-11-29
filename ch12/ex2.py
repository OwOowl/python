
class Car:
    color = ''
    speed = 0

    # 생성자
    def __init__(self):
        self.color = 'white'
        self.speed = 10

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value
        if self.speed < 0:
            self.speed = 0


myCar1 = Car()
myCar1.color = 'red'


myCar2 = Car()
myCar2.upSpeed(30)


print('자동차 1의 색상은 %s이며 현재 속도는 %dkm/h 입니다.' % (myCar1.color, myCar1.speed))
print('자동차 2의 색상은 %s이며 현재 속도는 %dkm/h 입니다.' % (myCar2.color, myCar2.speed))

