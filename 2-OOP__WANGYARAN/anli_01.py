
'''
定义一个学生类
'''
# 定义一个空的类
class Student():
    # 一个空类，pass表示直接跳过，占位用
    pass

# 定义一个对象
mingye = Student()


# 继续定义一个类，用来描述听python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    # 1 注意def缩进的层级
    # 2 系统默认一个self参数
    def doHomework(self):
        print("I 在做作业啊！")
        # 推荐在函数末尾使用return语句
        return None

#  实例化一个叫yueyue的学生，是一个具体的人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)

# 注意成员函数的调用没有传递进入参数
yueyue.doHomework()


