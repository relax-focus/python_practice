# 字符串------------------------------------------------------
# s1 = r'\'hello, world!\''
# s2 = r'\n\\hello, world!\\\n'
# print(s1, s2, end='')

# s1 = '\141\142\143\x61\x62\x63'
# s2 = '\u9a86\u660a'
# print(s1, s2)

# s1 = 'hello ' * 3
# print(s1)

# s2 = 'world'
# s1 += s2
# print(s1)

# print('ll' in s1)
# print('good' in s1)

# str2 = 'abc123456'
# print(str2[2])
# print(str2[2:5])
# print(str2[2:])
# print(str2[2::2])
# print(str2[::2])
# print(str2[::-1])
# print(str2[-3:-1])

# str1 = 'hello, world!'
# print(len(str1))
# print(str1.capitalize())
# print(str1.title())
# print(str1.upper())
# print(str1.find('or'))
# print(str1.find('shit'))
# print(str1.index('or'))
# print(str1.index('shit'))
# print(str1.startswith('He'))
# print(str1.startswith('hel'))
# print(str1.endswith('!'))
# print(str1.center(50, '*'))
# print(str1.rjust(50, ' '))
# print(str1.ljust(50, '*'))

# str2 = 'abc123456'
# print(str2.isdigit())
# print(str2.isalpha())
# print(str2.isalnum())
# str3 = '  jackfrued@126.com '
# print(str3)
# print(str3.strip())

# a, b = 5, 10
# print('%d * %d = %d' % (a, b, a*b))
# print('{0} * {1} = {2}'.format(a, b, a*b))
# print(f'{a} * {b} = {a*b}')


# 列表--------------------------------------------------------
# list1 = [1, 3, 5, 7, 100]
# print(list1)
# list2 = ['hello'] * 3
# print(list2)
# print(len(list2))
# print(list1[0])
# print(list1[4])
# print(list1[-1])
# print(list1[-3])
# list1[2] = 300
# print(list1)
# for index in range(len(list1)):
#     print(list1[index])

# for elem in list1:
#     print(elem)

# for index, elem in enumerate(list1):
#     print(index, elem)

# list1.append(200)
# list1.insert(1, 400)
# list1 += [1000, 2000]
# print(list1)
# print(len(list1))
# if 3 in list1:
#     list1.remove(3)
# if 1234 in list1:
#     list1.remove(1234)
# print(list1)
# list1.pop(1)
# print(list1)
# list1.clear()
# print(list1)

# fruits = ['grape', 'apple', 'strawberry', 'waxberry']
# fruits += ['pitaya', 'pear', 'mango']
# fruits2 = fruits[1:4]
# print(fruits2)
# fruits3 = fruits[:]
# print(fruits3)
# fruits4 = fruits[-3:-1]
# print(fruits4)
# fruits5 = fruits[::-1]
# print(fruits5)

# list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# list2 = sorted(list1)
# list3 = sorted(list1, reverse=True)
# list4 = sorted(list1, key=len)
# print(list1)
# print(list2)
# print(list3)
# print(list4)
# list1.sort(reverse=True)
# print(list1)


# 生成式和生成器-------------------------------------------
# import sys
# f = [x for x in range(1, 10)]
# print(f)
# f = [x + y for x in 'ABCDE' for y in '1234567']
# print(f)
# f = [x ** 2 for x in range(1, 1000)]
# print(sys.getsizeof(f))
# print(f)

# f = (x ** 2 for x in range(1, 1000))
# print(sys.getsizeof(f))
# print(f)
# for val in f:
#     print(val)

# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a+b
#         yield a

# def main():
#     for val in fib(20):
#         print(val)

# if __name__ == '__main__':
#     main()


# 元组------------------------------------------
# t = ('骆昊', 38, True, '四川成都')
# print(t)
# print(t[0])
# print(t[3])

# for member in t:
#     print(member)

# t = ('王大锤', 20, True, '云南昆明')
# print(t)

# person = list(t)
# print(person)

# person[0] = '李小龙'
# person[1] = 25
# print(person)

# fruits_list = ['apple', 'banana', 'orange']
# fruits_tuple = tuple(fruits_list)
# print(fruits_tuple)


# 集合----------------------------------------------
# set1 = {1, 2, 3, 3, 3, 2}
# print(set1)
# print('Length =', len(set1))
# set2 = set(range(1, 10))
# print(set2)
# set1.add(4)
# set1.add(5)
# set2.update([11, 12])
# print(set1)
# print(set2)
# set2.discard(5)
# if 4 in set2:
#     set2.remove(4)
# print(set2)

# for elem in set2:
#     print(elem ** 2, end=" ")
# print()

# set3 = set((1, 2, 3, 3, 2, 1))
# print(set3.pop())
# print(set3)
# print(set1)
# print(set2)
# # print(set1 & set2)
# # print(set1 | set2)
# # print(set2 - set1)
# # print(set1 ^ set2)
# print(set2 <= set1)
# print(set3 <= set1)
# print(set1 >= set2)
# print(set1 >= set3)


# 字典----------------------------------------------------------------------------
# scores = {'骆昊':95, '白元芳':78, '狄仁杰': 82}
# print(scores['骆昊'])
# print(scores['狄仁杰'])
# for elem in scores:
#     print('%s\t----->\t%d' % (elem, scores[elem]))

# scores['白元芳'] = 65
# scores['诸葛王朗'] = 71
# scores.update(冷面=67, 放弃=85)
# print(scores)
# if '武则天' in scores:
#     print(scores['武则天'])
# print(scores.get('武则天'))
# print(scores.get('武则天', 60))
# print(scores.popitem())
# print(scores.popitem())
# print(scores.pop('骆昊', 100))
# scores.clear()
# print(scores)


# 练习-----------------------------------------------------------------------
# 练习1：在屏幕上显示跑马灯文字。
# import os 
# import time

# def main():
#     content = '北京欢迎你，啦啦啦啦啦啦......'
#     while True:
#         os.system('cls')
#         print(content)
#         time.sleep(0.2)
#         content = content[1:] + content[0]

# if __name__ == '__main__':
#     main()

# 练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
# import random

# def generate_code(code_len=4):
#     """
#     生成指定长度的验证码
#     :param code_len: 验证码的长度(默认4个字符)
#     :return: 由大小写英文字母和数字构成的随机验证码
#     """
#     all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     last_pos = len(all_chars) - 1
#     code = ''
#     for _ in range(code_len):
#         index = random.randint(0, last_pos)
#         code += all_chars[index]
#     return code

# if __name__ == '__main__':
#     print(generate_code(10))

# 练习3：设计一个函数返回给定文件名的后缀名。
# def get_suffix(filename, has_dot=False):
#     """
#     获取文件名的后缀名
#     :param filename: 文件名
#     :param has_dot: 返回的后缀名是否需要带点
#     :return: 文件的后缀名
#     """
#     pos = filename.rfind('.')
#     if 0 < pos < len(filename) - 1:
#         index = pos if has_dot else pos + 1
#         return filename[index:]
#     else:
#         return ''

# if __name__ == '__main__':
#     print(get_suffix('liangxu.bat'))

# 练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。
# def max2(x):
#     m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
#     for index in range(2, len(x)):
#         if x[index] > m1:
#             m2 = m1
#             m1 = x[index]
#         elif x[index] > m2:
#             m2 = x[index]
#     return m1, m2

# if __name__ == '__main__':
#     list1 = [1,12,23,14,45,76,37,48,9]
#     print(max2(list1))

# 练习5：计算指定的年月日是这一年的第几天。
# def is_leap_year(year):
#     """
#     判断指定的年份是不是闰年

#     :param year: 年份
#     :return: 闰年返回True平年返回False
#     """
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

# def which_day(year, month, date):
#     """
#     计算传入的日期是这一年的第几天

#     :param year: 年
#     :param month: 月
#     :param date: 日
#     :return: 第几天
#     """
#     days_of_month = [
#         [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
#         [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     ][is_leap_year(year)]
#     total = 0
#     for index in range(month - 1):
#         total += days_of_month[index]
#     return total + date

# def main():
#     print(which_day(2019, 10, 16))

# if __name__ == '__main__':
#     main()

# 练习6：打印杨辉三角。
# def main():
#     num = int(input('Number of rows: '))
#     yh = [[]] * num
#     # print(yh)
#     for row in range(len(yh)):
#         yh[row] = [None] * (row + 1)
#         # print(yh[row])
#         for col in range(len(yh[row])):
#             if col == 0 or col == row:
#                 yh[row][col] = 1
#             else:
#                 yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
#             print(yh[row][col], end='\t')
#         print()

# if __name__ == '__main__':
#     main()


# 综合案例------------------------------------------------------------------
# 案例1：双色球选号。
# from random import randrange, randint, sample

# def display(balls):
#     """
#     输出列表中的双色球号码
#     """
#     for index, ball in enumerate(balls):
#         if index == len(balls) - 1:
#             print('|', end=' ')
#         print('%02d' % ball, end=' ')
#     print()

# def random_select():
#     """
#     随机选择一组号码
#     """
#     red_balls = [x for x in range(1, 34)]
#     selected_balls = []
#     selected_balls = sample(red_balls, 6)
#     selected_balls.sort()
#     selected_balls.append(randint(1, 16))
#     return selected_balls

# def main():
#     n = int(input('机选几注: '))
#     for _ in range(n):
#         display(random_select())

# if __name__ == '__main__':
#     main()


# 综合案例2：约瑟夫环问题。
# """
# 《幸运的基督徒》
# 有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
# """

# def main():
#     persons = [True] * 30
#     counter, index, number = 0, 0, 0
#     while counter < 15:
#         if persons[index]:
#             number += 1
#             if number == 9:
#                 persons[index] = False
#                 counter += 1
#                 number = 0
#         index += 1
#         # print(index)
#         index %= 30
#         # print(index, '\n')
#     for person in persons:
#         print('基' if person else '非', end='')

# if __name__ == '__main__':
#     main()


# 综合案例3：井字棋游戏。
import os

def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('cls')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('cls')
            print_board(curr_board)
        choice = input('再玩一局？(yes|no)')
        begin = choice == 'yes'

if __name__ == '__main__':
    main()