# -*- coding: utf-8 -*-
# time: 2022/7/5 10:04
# file: Data_serialization.py
# author: liwenzheng

"""
数据序列化三种
YAML XML JSON 
选用:
采用和支持:JSON = XML > YAML 
可读性:YAML > JSON > XML
读写速度:JSON > XML > YAML
文件大小:JSON > YAML > XML
流行 json > XML > YAML
基本使用
1. 基本的格式要求
大小写敏感；
使用缩进表示层级关系；
使用空格键缩进，而非Tab键缩进
缩进的空格数目不重要，只需要相同层级的元素左侧对齐；
文件中的字符串不需要使用引号标注，但若字符串包含有特殊字符则需用引号标注；
注释标识为#
2. 注释
YAML使用#作为注释，特别的是YAML中只有行注释。
3. 常量值
YAML中提供了多种常量结构，包括：整数，浮点数，字符串，NULL，日期，布尔，时间。
4. 对象
使用冒号代表，格式为key: value。冒号后面要加一个空格
可以使用缩进表示层级关系
5. 数组
使用一个短横线加一个空格代表一个数组项
6. 特殊符号
使用场景：
DevOps
Ansible：使用 YAML 描述远程基础架构的期望状态、管理配置和编排 IT 流程
Docker Compose：使用 YAML 来描述组成你的 Dockerized 应用程序的微服务
Kubernetes :使用 YAML 定义计算机集群中的各种对象来编排和管理
"""
import os,sys
#try:
#    from yaml import CSafeLoader as safe_load
#    from yaml import CSafeDumper as safe_dump
#except ImportError:
#    from yaml import safe_load
#    from yaml import safe_dump
#lass Data_serialization():
#   def __init__(self):
#       pass
#   def dump_yaml(self):
#       #python对象转存yaml
#       with open("/path/to/file.yaml", mode="wb") as file:
#           yaml.dump(data, file, encoding="utf-8")
#   def load_yaml(self):
#       # yaml解析成python对象
#       pass
import yaml
Current_path =os.path.abspath('.')
target_path = os.path.join(Current_path,'yaml_learn.yml')

with open(target_path,mode='r',encoding='utf-8') as yaml_data:
    work_data = yaml_data.read()

#s = yaml.load(work_data,Loader=yaml.CSafeLoader)
s = yaml.load_all(work_data,Loader=yaml.CSafeLoader)
print(s)
print(type(s))
