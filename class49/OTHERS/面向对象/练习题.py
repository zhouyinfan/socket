# 定义一个学生类。有下面的类属性：
# # 1 姓名
# # 2 年龄
# # 3 成绩（语文，数学，英语)[每课成绩的类型为整数]
# # 类方法：
# # 1 获取学生的姓名：get_name() 返回类型:str
# # 2 获取学生的年龄：get_age() 返回类型:int
# # 3 返回3门科目中最高分数的课程。get_course()
# # 4 返回该学生的平均成绩get_avg()
class student:
    sname="jack"
    sage=23
    sc={"语文":70,"数学":80,"英语":90}
    score=list(sc.values())
    def get_name(self):
        print("学生名字为：%s"%self.sname)
    def get_age(self):
        print("学生年龄为：%s"%self.sage)
    def get_course(self):
        max1=max(self.score)
        for i in self.sc:
            if self.sc[i]==max1:
                print("最高分的课程为：%s"%i)
    def get_avg(self):
        sum1=sum(self.score)
        avg=sum1/len(self.score)
        print("该学生的平均分为：%d"%avg)
s=student()
# s.get_name()
# s.get_age()
s.get_course()
s.get_avg()









