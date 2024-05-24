class Bb:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.total = 0

    def sell(self):
        print(self.name + "을", self.price, "에 팔았습니다.")
        self.total = 0 + self.price

    def eat(self):
        print(self.name + "을 먹었습니다.")

s = Bb("슈크림붕어빵", 1000)
p = Bb("팥붕어빵", 800)

s.sell()
s.eat()
p.sell()
p.eat()

print(s.total + p.total)

