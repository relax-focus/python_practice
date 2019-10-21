# 面向对象编程基础

# class Student(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def study(self, course_name):
#         print('%s正在学习%s.' % (self.name, course_name))

#     def watch_movie(self):
#         if self.age < 18:
#             print('%s只能观看《熊出没》.' % self.name)
#         else:
#             print('%s正在观看爱情动作片.' % self.name)

# def main():
#     stu1 = Student('骆昊', 38)
#     stu1.study('Python程序设计')
#     stu1.watch_movie()
#     stu2 = Student('王大锤', 15)
#     stu2.study('思想品德')
#     stu2.watch_movie()

# if __name__ == '__main__':
#     main()

# class Test:
#     def __init__(self, foo):
#         self.__foo = foo

#     def __bar(self):
#         print(self.__foo)
#         print('__bar')

# def main():
#     test = Test('hello')
#     test._Test__bar()
#     print(test._Test__foo)

# if __name__ == '__main__':
#     main()


# 练习--------------------------------------------------------
# 练习1：定义一个类描述数字时钟。
# import os
# from time import sleep

# class Clock(object):
#     """数字时钟"""

#     def __init__(self, hour=0, minute=0, second=0):
#         """初始化方法
#         :param hour: 时
#         :param minute: 分
#         :param second: 秒
#         """
#         self._hour = hour
#         self._minute = minute
#         self._second = second

#     def run(self):
#         """走字"""
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0

#     def show(self):
#         """显示时间"""
#         return '%02d:%02d:%02d' % \
#             (self._hour, self._minute, self._second)

# def main():
#     clock = Clock(23, 59, 58)
#     while True:
#         os.system('cls')
#         print(clock.show())
#         sleep(1)
#         clock.run()

# if __name__ == '__main__':
#     main()

# 练习2：定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。
from math import sqrt

class Point(object):
    def __init__(self, x=0, y=0):
        """初始化方法
        
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """移动到指定位置
        
        :param x: 新的横坐标
        "param y: 新的纵坐标
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """移动指定的增量
        
        :param dx: 横坐标的增量
        "param dy: 纵坐标的增量
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """计算与另一个点的距离
        
        :param other: 另一个点
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))

def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))

if __name__ == '__main__':
    main()