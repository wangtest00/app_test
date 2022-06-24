from appium import webdriver
import unittest,requests,time
from daiqian.base_fr import *
from daiqian.auth_fr import *
from data.var_fr import *
from app.grab_data_fr import *
from app.appium_adb import *
from app.swipe_test import *
from app.initDevices import *
from data.path_fr import *



class Test_Install_Login_Fr(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # 在所有用例执行之前运行的
        print('我是setUpclass，我位于所有用例的开始')
        adb_connect(devices_info_vivo['udid'])     # 连接wifi调试
        huanxing_screen(devices_info_vivo['udid']) # 唤醒屏幕
        sildes(devices_info_vivo['udid'], 360, 1400, 360, 1000, 50)          # adb向上滑屏
        uninstall_app(devices_info_vivo['udid'], devices_info_vivo['appPackage'])  # 预先卸载app包
        appium_start('127.0.0.1', port_vivo)  # 启动appium服务

    def setUp(self):
        '''每条testcase执行前初始化'''
        print('testcase setUp')
        self.driver = devices_object_vivo.init_devices(port_vivo, devices_info_vivo)
        # 设置隐式等待为 10s,一旦设置了隐式等待，它则会在整个Web Driver对象的实例声明周期中。
        self.driver.implicitly_wait(10)
    def test_install_login(self):
        '''【FeriaRapida-android-VIVO】test_install_login-登录-设置密码,授权-正案例'''
        input1=self.driver.find_element_by_xpath(xp1)
        input1.send_keys('8585850000')
        self.driver.find_element_by_xpath(xp2)
        input2=self.driver.find_element_by_xpath(xp3)
        input2.send_keys('5555')
        time.sleep(3)
        input3=self.driver.find_element_by_xpath(xp4)
        input3.send_keys('123456')
        time.sleep(3)
        input4=self.driver.find_element_by_xpath(xp5)
        input4.send_keys('123456')
        time.sleep(3)
        shouquan_vivo(self.driver)
        time.sleep(3)
    def test_install_first_apply(self):
        '''【FeriaRapida-android-VIVO】test_install_first_apply-登录-设置密码，授权，进件5页面，检查数据抓取正案例'''
        registNo=str(random.randint(7000000000,9999999999)) #10位随机数作为手机号
        print(registNo)
        self.driver.find_element_by_xpath(xp1).send_keys(registNo)
        time.sleep(1)
        code = compute_code(registNo)
        self.driver.find_element_by_xpath(xp2)
        self.driver.find_element_by_xpath(xp3).send_keys(code)
        self.driver.find_element_by_xpath(xp4).send_keys('123456')
        self.driver.find_element_by_xpath(xp5).send_keys('123456')
        self.driver.implicitly_wait(10)
        shouquan_vivo(self.driver)
        time.sleep(3)
        self.driver.find_element_by_xpath(xp6).click()  # step1点击申请贷款按钮,进入实名认证页面
        self.driver.find_element_by_xpath(xp7).click()  # 问卷页面
        self.driver.find_element_by_xpath(xp8).send_keys('lll')
        self.driver.find_element_by_xpath(xp9).send_keys('test')
        self.driver.find_element_by_xpath(xp10).send_keys('android')
        self.driver.find_element_by_xpath(xp11).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(xp12).click()  #点击ok
        time.sleep(3)
        self.driver.find_element_by_xpath(xp13).click()  #点击ok
        time.sleep(3)
        self.driver.find_element_by_xpath(xp14).click()  #marital status婚姻状况
        time.sleep(3)
        self.driver.find_element_by_xpath(xp15).click()  #点击ok
        swipeup(self.driver,1000)
        self.driver.implicitly_wait(10)
        Curp=certlist()
        self.driver.find_element_by_xpath(xp16).send_keys(Curp)  #curp
        self.driver.find_element_by_xpath(xp17).send_keys('test')
        time.sleep(3)
        self.driver.find_element_by_xpath(xp18).send_keys('test')
        time.sleep(3)
        self.driver.find_element_by_xpath(xp19).send_keys('test')
        time.sleep(3)
        self.driver.find_element_by_xpath(xp20).send_keys('test')
        time.sleep(3)
        self.driver.find_element_by_xpath(xp21).send_keys('test')
        time.sleep(3)
        self.driver.find_element_by_xpath(xp22).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(xp23).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(xp24).click()  #step2点击下一步,进入kyc页面
        time.sleep(3)
        self.driver.find_element_by_xpath(xp25).click()
        self.driver.find_element_by_xpath(xp26).click()
        self.driver.find_element_by_xpath(xp27).click()
        self.driver.find_element_by_xpath(xp28).click()
        self.driver.find_element_by_xpath(xp29).click()
        self.driver.find_element_by_xpath(xp30).click()
        self.driver.find_element_by_xpath(xp31).click() #step3点击下一步，进入工作信息页面
        time.sleep(5)
        self.driver.find_element_by_xpath(xp32).click()
        self.driver.find_element_by_xpath(xp33).click()
        self.driver.find_element_by_xpath(xp34).click()#step4点击下一步,进入联系人页面
        time.sleep(5)
        self.driver.find_element_by_xpath(xp35).click()
        self.driver.find_element_by_xpath(xp36).click()
        self.driver.find_element_by_xpath(xp37).click()
        self.driver.find_element_by_xpath(xp38).click()
        self.driver.find_element_by_xpath(xp39).click()
        self.driver.find_element_by_xpath(xp40).click()
        self.driver.find_element_by_xpath(xp41).click()
        self.driver.find_element_by_xpath(xp42).click()
        self.driver.find_element_by_xpath(xp43).click()
        grab_data=cx_grab_data(registNo)
        for i in range(len(grab_data)):
            self.assertIsNotNone(grab_data[i])
        logout(self.driver)
    def tearDown(self):
        #self.driver.quit()
        print("testcase done")
    @classmethod
    def tearDownClass(cls):  # 在所有用例都执行完之后运行的
        adb_disconnect(devices_info_vivo['udid'])
        appium_stop(port_vivo)
        print('我是tearDownClass，我位于多有用例运行的结束')

if __name__ == '__main__':
    unittest.main()