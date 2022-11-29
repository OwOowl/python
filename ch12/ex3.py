
class Car:
    color = ''
    speed = 0

    # 생성자. 오버로딩 불가능
    def __init__(self, var1, var2):
        self.speed = var1
        self.color = var2

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value
        if self.speed < 0:
            self.speed = 0


myCar3 = Car(50, 'orange')

print('자동차 3의 색상은 %s이며 현재 속도는 %dkm/h 입니다.' % (myCar3.color, myCar3.speed))
