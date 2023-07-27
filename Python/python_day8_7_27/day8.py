class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
    
    def info(self):
        print(f'Model : {self.model}, Color : {self.color}')
    def aaa(self):
        print('Car')

class CarDrive(Car):
    def __init__(self, model, color, speed):
        # Car.__init__(self, model, color)
        # self.model = model
        # self.color = color
        # self.speed = speed
        super().__init__(model, color)
        self.speed = speed
        # self.speed = int(speed) if speed else 50 
        try:
            self.speed = int(speed)  # 입력된 속도값을 숫자로 변환
        except ValueError:
            self.speed = 50 
    ##입력을 받으면 기본인자가 작동이 안된다.
    ##기본 인자를 쓰고싶으면 if else를 통해 반환
    def aaa(self):
        print('CarDrive')
    
    def speedchange(self):
        print(f'speedchange : {self.speed}')

model1 = (input('차종을 입력: '))
color1 = (input('색깔을 입력: '))
speed1 = (input('속도를 입력: '))
car1 = CarDrive(model1, color1, speed1)

#1. info메서드 호출
car1.info()
#2. speedchange 메서드 호출
car1.speedchange()
car1.aaa()