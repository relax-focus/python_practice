# 面向对象进阶

# class Person(object):
#     __slots__ = ('_name', '_age', '_gender')

#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     # 访问器 - getter方法
#     @property
#     def name(self):
#         return self._name

#     # 访问器 - getter方法
#     @property
#     def age(self):
#         return self._age

#     # 修改器 - setter方法
#     @age.setter
#     def age(self, age):
#         self._age = age

#     def play(self):
#         if self._age <= 16:
#             print('%s正在玩飞行棋.' % self._name)
#         else:
#             print('%s正在玩斗地主.' % self._name)

# def main():
#     person = Person('王大锤', 12)
#     person.play()
#     person.age = 22
#     person.play()
#     print(person.name)

# if __name__ == '__main__':
#     main()

# 静态方法和类方法
# from math import sqrt

# class Triangle(object):
#     def __init__(self, a, b, c):
#         self._a = a
#         self._b = b
#         self._c = c

#     @staticmethod
#     def is_valid(a, b, c):
#         return a + b > c and b + c > a and a + c > b

#     def perimeter(self):
#         return self._a + self._b + self._c

#     def area(self):
#         half = self.perimeter() / 2
#         return sqrt(half * (half - self._a) *
#                     (half - self._b) * (half - self._c))

# def main():
#     a, b, c = 3, 4, 5
#     # 静态方法和类方法都是通过给类发消息来调用的
#     if Triangle.is_valid(a, b, c):
#         t = Triangle(a, b, c)
#         print(t.perimeter())
#         print(t.area())
#     else:
#         print('无法构成三角形.')

# if __name__ == '__main__':
#     main()

# from time import time, localtime, sleep

# class Clock(object):
#     """数字时钟"""

#     def __init__(self, hour=0, minute=0, second=0):
#         self._hour = hour
#         self._minute = minute
#         self._second = second

#     @classmethod
#     def now(cls):
#         ctime = localtime(time())
#         return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

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
#     clock = Clock.now()
#     while True:
#         print(clock.show())
#         sleep(1)
#         clock.run()

# if __name__ == '__main__':
#     main()

# 继承和多态

# class Person(object):
#     """人"""

#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     @property
#     def name(self):
#         return self._name

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, age):
#         self._age = age

#     def play(self):
#         print('%s正在愉快的玩耍.' % self._name)

#     def watch_av(self):
#         if self._age >= 18:
#             print('%s正在观看爱情动作片.' % self._name)
#         else:
#             print('%s只能观看《熊出没》.' % self._name)

# class Student(Person):
#     """学生"""

#     def __init__(self, name, age, grade):
#         super().__init__(name, age)
#         self._grade = grade

#     @property
#     def grade(self):
#         return self._grade

#     @grade.setter
#     def grade(self, grade):
#         self._grade = grade

#     def study(self, course):
#         print('%s的%s正在学习%s.' % (self._grade, self._name, course))

# class Teacher(Person):
#     """老师"""

#     def __init__(self, name, age, title):
#         super().__init__(name, age)
#         self._title = title

#     @property
#     def title(self):
#         return self._title

#     @title.setter
#     def title(self, title):
#         self._title = title

#     def teach(self, course):
#         print('%s%s正在讲%s.' % (self._name, self._title, course))

# def main():
#     stu = Student('王大锤', 15, '初三')
#     stu.study('数学')
#     stu.watch_av()
#     t = Teacher('骆昊', 38, '专家')
#     t.teach('Python程序设计')
#     t.watch_av()

# if __name__ == '__main__':
#     main()

# from abc import ABCMeta, abstractmethod

# class Pet(object, metaclass=ABCMeta):
#     """宠物"""
#     def __init__(self, nickname):
#         self._nickname = nickname

#     @abstractmethod
#     def make_voice(self):
#         """发出声音"""
#         pass

# class Dog(Pet):
#     """狗"""
#     def make_voice(self):
#         print('%s:汪汪汪...' % self._nickname)

# class Cat(Pet):
#     """猫"""
#     def make_voice(self):
#         print('%s:喵...喵...' % self._nickname)

# def main():
#     pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
#     for pet in pets:
#         pet.make_voice()

# if __name__ == '__main__':
#     main()


# 综合案例
# 案例1：奥特曼打小怪兽。
# from abc import ABCMeta, abstractmethod
# from random import randint, randrange

# class Fighter(object, metaclass=ABCMeta):
#     """战斗者"""
#     __slots__ = ('_name', '_hp')

#     def __init__(self, name, hp):
#         """初始化方法

#         :param name: 名字
#         :param hp: 生命值
#         """
#         self._name = name
#         self._hp = hp

#     @property
#     def name(self):
#         return self._name

#     @property
#     def hp(self):
#         return self._hp

#     @hp.setter
#     def hp(self, hp):
#         self._hp = hp if hp >= 0 else 0

#     @property
#     def alive(self):
#         return self._hp > 0

#     @abstractmethod
#     def attack(self, other):
#         """攻击

#         :param other: 被攻击的对象
#         """
#         pass

# class Ultraman(Fighter):
#     """奥特曼"""
#     __slots__ = ('_name', '_hp', '_mp')

#     def __init__(self, name, hp, mp):
#         """初始化方法

#         :param name: 名字
#         :param hp: 生命值
#         :param mp: 魔法值
#         """
#         super().__init__(name, hp)
#         self._mp = mp

#     def attack(self, other):
#         other.hp -= randint(15, 25)

#     def huge_attack(self, other):
#         """究极必杀技(打掉对方至少50点或四分之三的血)

#         :param other: 被攻击的对象

#         :return: 使用成功返回True否则返回False
#         """
#         if self._mp >= 50:
#             self._mp -= 50
#             injury = other.hp * 3 // 4
#             injury = injury if injury >= 50 else 50
#             other.hp -= injury
#             return True
#         else:
#             self.attack(other)
#             return False

#     def magic_attack(self, others):
#         """魔法攻击

#         :param others: 被攻击的群体

#         :return: 使用魔法成功返回True否则返回False
#         """
#         if self._mp >= 20:
#             self._mp -= 20
#             for temp in others:
#                 if temp.alive:
#                     temp.hp -= randint(10, 15)
#             return True
#         else:
#             return False

#     def resume(self):
#         """恢复魔法值"""
#         incr_point = randint(1, 10)
#         self._mp += incr_point
#         return incr_point

#     def __str__(self):
#         return '~~~%s奥特曼~~~\n' % self._name + \
#             '生命值：%d\n' % self._hp + \
#             '魔法值：%d\n' % self._mp

# class Monster(Fighter):
#     """小怪兽"""
#     __slots__ = ('_name', '_hp')

#     def attack(self, other):
#         other.hp -= randint(10, 20)

#     def __str__(self):
#         return '~~~%s小怪兽~~~\n' % self._name + \
#             '生命值：%d\n' % self._hp

# def is_any_alive(monsters):
#     """判断有没有小怪兽是活着的"""
#     for monster in monsters:
#         if monster.alive > 0:
#             return True
#     return False

# def select_alive_one(monsters):
#     """选中一只活着的小怪兽"""
#     monsters_len = len(monsters)
#     while True:
#         index = randrange(monsters_len)
#         monster = monsters[index]
#         if monster.alive > 0:
#             return monster

# def display_info(ultraman, monsters):
#     """显示奥特曼和小怪兽的信息"""
#     print(ultraman)
#     for monster in monsters:
#         print(monster, end='')

# def main():
#     u = Ultraman('骆昊', 1000, 120)
#     m1 = Monster('狄仁杰', 250)
#     m2 = Monster('白元芳', 500)
#     m3 = Monster('王大锤', 750)
#     ms = [m1, m2, m3]
#     fight_round = 1
#     while u.alive and is_any_alive(ms):
#         print('========第%02d回合========' % fight_round)
#         m = select_alive_one(ms)
#         skill = randint(1, 10)
#         if skill <= 6:
#             print('%s使用普通攻击打了%s.' % (u.name, m.name))
#             u.attack(m)
#             print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
#         elif skill <= 9:
#             if u.magic_attack(ms):
#                 print('%s使用了魔法攻击.' % u.name)
#             else:
#                 print('%s使用了魔法失败.' % u.name)
#         else:
#             if u.huge_attack(m):
#                 print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
#             else:
#                 print('%s使用普通攻击打了%s.' % (u.name, m.name))
#                 print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))

#         if m.alive > 0:
#             print('%s回击了%s.' % (m.name, u.name))
#             m.attack(u)
#         display_info(u, ms)
#         fight_round += 1
#     print('\n========战斗结束!========\n')
#     if u.alive > 0:
#         print('%s奥特曼胜利!' % u.name)
#     else:
#         print('小怪兽胜利!')

# if __name__ == '__main__':
#     main()


# 案例2：扑克游戏。
import random

class Card(object):
    """一张牌"""
    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def face(self):
        return self._face

    @property
    def suite(self):
        return self._suite

    def __str__(self):
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%s%s' % (self._suite, face_str)

    def __repr__(self):
        return self.__str__()

class Poker(object):
    """一副牌"""
    def __init__(self):
        self._cards = [Card(suite, face)
                        for suite in '♠♥♣♦'
                        for face in range(1, 14)]
        self._current = 0
    
    @property
    def cards(self):
        return self._cards
    
    def shuffle(self):
        """洗牌（随机乱序）"""
        self._current = 0
        random.shuffle(self._cards)

    @property
    def next(self):
        """发牌"""
        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌"""
        return self._current < len(self._cards)

class Player(object):
    """玩家"""
    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []

    @property
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    def get(self, card):
        """摸牌"""
        self._cards_on_hand.append(card)

    def arrange(self, card_key):
        """玩家整理手上的牌"""
        self._cards_on_hand.sort(key=card_key)

def get_key(card):
    return (card.suite, card.face)

def main():
    p = Poker()
    p.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    for _ in range(13):
        for player in players:
            player.get(p.next)

    for player in players:
        print(player.name + ':', end=' ')
        player.arrange(get_key)
        print(player.cards_on_hand)

if __name__ == '__main__':
    main()