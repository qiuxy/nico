__author__ = 'qiuxy'
import sys


class Control(object):
    def __init__(self, argv=None):
        self.argv = argv or sys.argv[:]

    def execute(self):
        func = self.argv[1]
        if func == 'pwd':
            from pwd import myPwd

            pwd = myPwd.pwd(sys.argv)
            pwd.execute()
        elif func == 'test':
            print('test')
        else:
            print('this function[' + func + '] does not exist...')
