from appium import webdriver
import unittest,os,time,requests
from data.var_third import *
from app.appium_adb import *
from app.swipe_test import *
from app.initDevices import *

#增加重试连接次数
# requests.DEFAULT_RETRIES = 2
# #关闭多余的链接：requests使用了urllib3库，默认的http connection是keep-alive的，requests设置False关闭
# s = requests.session()
# s.keep_alive = False

class Test_iMaoTai_Oppo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('我是setUpclass，我位于所有用例的开始（只执行一次）')
        adb_connect(devices_info_moutai['udid'])                      #连接wifi调试
        huanxing_screen(devices_info_moutai['udid'])                  #唤醒屏幕
        sildes(devices_info_moutai['udid'],360, 1400, 360, 1300, 50)  #adb向上滑屏
        appium_start('127.0.0.1', port_moutai)                        #启动appium服务
    def setUp(self):
        '''每条testcase执行前初始化'''
        print('testcase begin')
        self.driver=devices_object_moutai.init_devices(port_moutai, devices_info_moutai)
        #设置隐式等待为 10s,一旦设置了隐式等待，它则会在整个Web Driver对象的实例声明周期中。
        self.driver.implicitly_wait(10)
        swipeup(self.driver,1000)
    def test_shengou(self):
        ''''茅台预约申购-每天9~10点开放申购通道'''
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ImageView').click()
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView').click()
        #点击预约申购
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button').click()
        #点击第2件商品申购
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button').click()
        swipeup(self.driver, 1000)

    def tearDown(self):
        self.driver.quit()
        print("testcase done")
    @classmethod
    def tearDownClass(cls):
        adb_disconnect(devices_info_moutai['udid'])
        appium_stop(port_moutai)
        print('我是tearDownClass，我位于所有用例运行的结束（只执行一次）')

if __name__ == '__main__':
    unittest.main()