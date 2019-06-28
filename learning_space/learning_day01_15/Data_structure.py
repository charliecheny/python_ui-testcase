# yield 生成器生成斐波那契数列
# yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，
# Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，
# 而是返回一个 iterable 对象！在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，
# 执行到 yield b 时，fab 函数就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句继续执行，
# 而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield。
# 看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield
# 返回当前的迭代值。
import os
import time
import random
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
        yield a

def main1():
    for val in fib(4):
        print(val)
# 跑马灯文字
def test():
    content = "上海欢迎你，，，欢迎你。。。。"
    while True:
        os.system("cls")
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]
# 生成验证码
def generate_code(code_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyz'
    code = ''
    for _ in range(code_len):
        index = random.randint(0, len(all_chars) - 1)
        code += all_chars[index]
    return code

# 生成双色球号码
def display(balls):
    # 输出列表中的双色球号码
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%2d' % ball, end=' ')
    print()
def random_select():
    # 随机选择一组号码
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    # sample(list, k) 从总体序列或集合中选择k个唯一随机元素
    # 选择6个红色球（1-33）
    selected_balls = random.sample(red_balls, 6)
    selected_balls.sort()
    # 选择1个蓝色球（1-16）
    selected_balls.append(random.randint(1, 16))
    return selected_balls
def lottery_ticket():
    # 机选n注彩票
    n = int(input('机选几注：'))
    for _ in range(n):
        display(random_select())



if __name__ == '__main__':
    lottery_ticket()




