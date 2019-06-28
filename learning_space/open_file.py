
import fileinput
class Open_File:
    def demo_one(self):
        # 使用readline函数
        file = open("./UI_autotest_Special-treatment", 'r', encoding='utf-8')
        line = file.readline()
        while line:
            print(line, end='')
            line = file.readline()
        file.close()

    def demo_two(self):
        # 一次性读取多行数据
        file = open("./UI_autotest_Special-treatment", 'r', encoding='utf-8')
        while 1:
            lines =file.readlines(200)
            if not lines:
                break
            for line in lines:
                print(line)
        file.close()

    def demo_three(self):
        # 使用for循环(文件一直没有关闭，耗内存)
        for line in open("./UI_autotest_Special-treatment", 'r', encoding='utf-8'):
            print(line)

    def demo_four(self):
        # 使用fileinput模块
        for line in fileinput.input("./UI_autotest_Special-treatment", 'r'):
            print(line)




















