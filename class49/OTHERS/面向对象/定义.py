class Student:
    a="suke"
    print("skin='yellow'")
    def listen(self):
        b="jack"
        print("%s  听课中。。。"%b)
        return b
    def test(self):
        print("%s考试中。。。"%self.a)
    def summary(self):
        b=self.listen()
        print("%s总结中。。。"%b)
s=Student()
# s.listen()
# s.test()
# s.summary()
# print("%s 在吃饭"%s.listen())