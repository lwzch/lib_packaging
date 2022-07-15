# _*_ coding: utf-8 _*_
# time: 2022/7/11 15:43
# file: grammar_tiaoshi.py
# author: liwenzheng

def gentor():
    yield 2
def fib():
    a, b = 1, 1
    num = 1
    while True:
        yield a
        num +=1
        a, b = b, a+b
        if num == 10:
            break
num = fib()
for i in num:
    print(i)
def intNum():
    print("开始执行")
    for i in range(5):
        yield i
        print("继续执行")
#num = intNum()
##调用 next() 内置函数
#print(next(num))
##调用 __next__() 方法
#print(num.__next__())
##通过for循环遍历生成器
#for i in num:
#    print(i)

from pathlib import Path

print(Path.cwd())
print(Path.)

