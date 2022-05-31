from appium import webdriver
import unittest,os,time,requests
from data.var_tiktok import *
from app.appium_adb import *
from app.swipe_test import *
from app.initDevices import *

#增加重试连接次数
# requests.DEFAULT_RETRIES = 2
# #关闭多余的链接：requests使用了urllib3库，默认的http connection是keep-alive的，requests设置False关闭
# s = requests.session()
# s.keep_alive = False

class Test_TikTok_Oppo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('我是setUpclass，我位于所有用例的开始（只执行一次）')
        adb_connect(devices_info_oppo['udid'])                      #连接wifi调试
        huanxing_screen(devices_info_oppo['udid'])                  #唤醒屏幕
        sildes(devices_info_oppo['udid'],360, 1400, 360, 1300, 50)  #adb向上滑屏
        appium_start('127.0.0.1', port_oppo)                        #启动appium服务
    def setUp(self):
        '''每条testcase执行前初始化'''
        print('testcase begin')
        self.driver=devices_object_oppo.init_devices(port_oppo, devices_info_oppo)
        #设置隐式等待为 10s,一旦设置了隐式等待，它则会在整个Web Driver对象的实例声明周期中。
        self.driver.implicitly_wait(10)
        swipeup(self.driver,1000)
    def test_001(self):
        for i in range(10):
            print("第{}次向上滑动".format(i+1))
            time.sleep(10)
            swipeup(self.driver,1000)
    def tearDown(self):
        self.driver.quit()
        print("testcase done")
    @classmethod
    def tearDownClass(cls):
        adb_disconnect(devices_info_oppo['udid'])
        appium_stop(port_oppo)
        print('我是tearDownClass，我位于所有用例运行的结束（只执行一次）')

# if __name__ == '__main__':
#     unittest.main()