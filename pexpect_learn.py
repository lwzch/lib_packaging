# -*- coding: utf-8 -*-
"""
Pexpect Expect 程序主要用于人机对话的模拟，就是那种系统提问，人来回答 yes/no python语言是pexpect.
主要使用三个方法
1、spawn() 方法用来执行一个程序，它返回这个程序的操作句柄。
logfile=None：指定日志文件，可指定为sys.stdout
2、expect()方法 等待指定的关键字。正则匹配 返回 0 表示匹配到了所需的关键字
before/after/match：获取程序运行输出
3、发送信息的部分方法 
    send() 信息
    sendline() 信息+回车
    sendcontrol() 发送控制信号(ctrl+C)
    sendintr() 发送终止信号
使用场景:
1、SSH登录
"""

from pty import spawn
from pexpect import *
spawn

s=spawn("ls -l")
s.expect(".py")
s.sendline("nihao")



