import unittest,io,sys
from BeautifulReport import BeautifulReport as bf  #导入BeautifulReport模块，这个模块也是生成报告的模块，但是比HTMLTestRunner模板好看
#from HTMLTestRunner_Chart import HTMLTestRunner
from XTestRunner import HTMLTestRunner
from data.common_path import *

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gb18030")

def load_all_case():
    discover=unittest.defaultTestLoader.discover(case_path,pattern='Test_Install_First_Apply_Tur_Oppo.py')
    return discover

if __name__=='__main__':
    suit=load_all_case()
    with(open(report_path+'/Turrant_Test_Reports2.html', 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title='Turrant_Test_Reports2',
            description='Turrant_Ui_Auto_Test2',
            language='en',
        )
        runner.run(
            testlist=suit,
            rerun=0,#失败后重试次数
            save_last_run=False
        )