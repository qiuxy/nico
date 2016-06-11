# coding:utf-8
__author__ = 'qiuxy'

import random


class pwd:
    def __init__(self, argv=None):
        self.pwds = ('abcdefhijklmnopqrstuvwxyzABCDEFHIJKLMNOPQRSTUVWXYZ0123456789', 'abcdefhijklmnopqrstuvwxyz',
                     'ABCDEFHIJKLMNOPQRSTUVWXYZ', 'abcdefhijklmnopqrstuvwxyzABCDEFHIJKLMNOPQRSTUVWXYZ',
                     '0123456789',
                     'abcdefhijklmnopqrstuvwxyzABCDEFHIJKLMNOPQRSTUVWXYZ0123456789_#$@')
        self.help = 0
        try:
            self.type = argv[2]
            if self.type == 'help' or self.type == '-h':
                self.help = 1
            else:
                type = int(argv[2])
                if type >= len(self.pwds):
                    print('parameter out of range... using default values[0]...')
                    self.type = 0
                self.type = int(argv[2])
        except:
            print('type parameter error... using default values[0]...')
            self.type = 0
        if self.help != 1:
            try:
                self.length = int(argv[3])
            except:
                print('length parameter error... using default values[10]...')
                self.length = 10

    def execute(self):
        if self.help == 1:
            self.pwdhelp()
        else:
            self.outputpwd()

    def outputpwd(self):
        length = 0
        pwds = self.pwds[int(self.type)]
        pwd = ''
        while (length < self.length):
            pwd = pwd + pwds[random.randint(0, len(pwds) - 1)]
            length = length + 1
        print(pwd)

    def pwdhelp(self):
        print('==========PWD1.0 HELP==========')
        print('使用方式: python util.py pwd type length')
        print('参数默认值type=0,length=10,如参数有问题则使用默认值')
        print('type列表:')
        print('0: 数字字母大小写混合')
        print('1: 小写字母')
        print('2: 大写字母')
        print('3: 大小写字母')
        print('4: 纯数字')
        print('5: 强密码包含字符[_#$@]')
        print('=======================')
