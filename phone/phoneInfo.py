# coding:utf-8
__author__ = 'qiuxy'
from external.baiduAPI import baiduAPI


class phone:
    def __init__(self, argv=None):
        self.help = 0
        try:
            self.type = argv[2]
            if self.type == 'help' or self.type == '-h':
                self.help = 1
            else:
                self.type = int(argv[2])
                self.inputPath = argv[3]
                self.outputPath = argv[4]
        except:
            print('parameter error... exit...')
            # TODO...
            return

    def getinfo(self):
        inputFile = open(self.inputPath)
        outputFile = open(self.outputPath, 'a')
        for phone in inputFile:
            print(baiduAPI.mobilenumber(phone), file=outputFile)
        inputFile.close()
        outputFile.close()

    def execute(self):
        if self.help == 1:
            self.phonehelp()
        else:
            self.getinfo()

    def phonehelp(self):
        print('==========PHONE1.0 HELP==========')
        print('使用方式: python util.py phone type inputPath outputPath')
        print('type列表:')
        print('1: 批量查询inputFile文件中的手机号归属地输出到outputFile')
        print('=======================')
