class Fruit_Operation:
    b="可生吃"
    __a="不可生吃"
    # print(__a)
    def __init__(self):
        print(self.b)
        print("水果操作")
    def __eat(self):
        print("吃水果")
    @staticmethod
    def fry():
        print("榨水果")
    def __del__(self):
        self.__eat()
        print("析构方法")
s=Fruit_Operation()
# s.fry()
# s._Fruit_Operation__eat()
print(s.b)
print(s.__a)
