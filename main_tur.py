import unittest,os,io,sys
from BeautifulReport import BeautifulReport as bf  #导入BeautifulReport模块，这个模块也是生成报告的模块，但是比HTMLTestRunner模板好看
from XTestRunner import HTMLTestRunner
from unittestreport import TestRunner
from data.var_turrant import *


#jenkins使用编码
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gb18030")

def load_all_case():
    discover=unittest.defaultTestLoader.discover(case_path,pattern='Test_Install_First_Apply_Tur_Oppo.py')
    return discover

if __name__=='__main__':
    suite=load_all_case()
    # 执行用例
    runner = TestRunner(suite,
                        filename='App_Test_Reports.html',
                        title='App_Test_Reports',
                        tester='WANGSHUANG',
                        desc="India_Ui_Auto_Test",
                        templates=1
                        )
    # 指定三个线程运行测试用例
    runner.run(thread_count=3)