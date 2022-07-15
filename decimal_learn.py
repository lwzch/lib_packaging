# -*- coding: utf-8 -*-
"""
Decimal 十进制浮点运算支持，自定义精度。
传参:整型、字符串
使用场景:
1、在对数据要求特别精确的场合(例如财务结算）    精度提升，性能下降，运行效率慢。
2、大规模的科学计算 float 
常用方法
1、浮点数转Decimal类型
2、getcontext().prec 设置有效数字的个数 精度
3、四舍五入，保留几位小数
4、Decimal 结果转化为string
5、十进制数学计算
"""

from decimal import *
class Decimal_operations(object):
    pass
