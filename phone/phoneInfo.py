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
                if len(argv) == 5:
                    self.column = '0'
                else:
                    self.column = str(argv[5])
        except:
            print('parameter error... exit...')
            exit()

    def getinfo(self):
        inputFile = open(self.inputPath)
        outputFile = open(self.outputPath, 'a')
        for phone in inputFile:
            info = baiduAPI.mobilenumber_format(baiduAPI.mobilenumber(phone), self.column)
            if info == 'error':
                info = phone.replace('\n', '') + '查询错误'
            print(info, file=outputFile)
        inputFile.close()
        outputFile.close()

    def execute(self):
        if self.help == 1:
            self.phonehelp()
        else:
            self.getinfo()

    def phonehelp(self):
        print('==========PHONE1.1 HELP==========')
        print('使用方式: python util.py phone type inputPath outputPath [column]')
        print('type列表:')
        print('1: 批量查询inputFile文件中的手机号归属地输出到outputFile')
        print('column要展示的字段列表:')
        print('0: 默认值全部展示 可不传')
        print('1: phone 手机号')
        print('2: prefix 前7位')
        print('3: province 省份')
        print('4: suit 号段')
        print('5: city 城市')
        print('6: supplier 运营商')
        print('例: column参数传入1356 即为输出手机号,省份,城市,运营商')
        print('=======================')
