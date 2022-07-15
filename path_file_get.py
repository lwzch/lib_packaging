# __*__ coding: UTF-8 __*__

from importlib.resources import path
import os,sys
from pathlib import Path

class File_path():
    """
    针对当前工作目录对路径的操作
    """
    def __init__(self):
        pass
    def path_mkdir(self,path,file):
        pass
    def path_delete(self):
        pass
    def path_check(self):
        pass
    def path_to_files(self,target_path,pat):
        self._path_ob = Path(target_path)
        path_object = self._path_ob.rglob(pat)
        for i in path_object:
            print(i)
    def path_current(self):
        return self._p.cwd()

if __name__ == '__main__':
    d =File_path()
    #d.path_to_files()
    #d.path_check()
    d.path_to_files('D:\gittest_lwz_learn\lib_learn','*')