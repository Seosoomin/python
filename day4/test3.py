class Unit:
    count = 0
    
    def __init__(self, name):
        count = Unit.count + 1
        self.name = name

    def move(self):
        print("이동합니다")

    def speak(self):
        print("꾸어엉")

class Dron(Unit):
    def speak(self):
        print("미네랄")

class Hydra(Unit):
    def speak(self):
        print("럴커업급좀")


d1 = Dron("드론1")
d2 = Dron("드론2")
h1 = Hydra("히드라1")
h2 = Hydra("히드라2")

d1.move()
d1.speak()
h2.move()
h2.speak()

print("현재 인구 수 : %d" % (Unit.count))
