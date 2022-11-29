
class Car:
    speed = 0

    def upSpeed(self, value):
        self.speed += value
        print('현재 속도(슈퍼 클래스) : %d' % self.speed)


# 상속
class Sedan(Car):
    def upSpeed(self, value):
        self.speed += value
        if self.speed > 150:
            self.speed = 150
        print('현재 속도(서브 클래스) : %d' % self.speed)


class Truck(Car):
    # 오버라이딩 할 필요가 없을 때
    pass


sedan1 = Sedan()
truck1 = Truck()

sedan1.upSpeed(200)
truck1.upSpeed(200)
