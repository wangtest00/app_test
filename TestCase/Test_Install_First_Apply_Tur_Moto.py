from appium import webdriver
import unittest,requests,time
from daiqian.base_lp import *
from app.auth_tur import *
from data.var_tur_app import *
from app.grab_data import *
from app.appium_adb import *
from app.swipe_test import *
from app.initDevices import *
from data.common_path_tur import *

# #增加重试连接次数
# requests.DEFAULT_RETRIES = 2
# #关闭多余的链接：requests使用了urllib3库，默认的http connection是keep-alive的，requests设置False关闭
# s = requests.session()
# s.keep_alive = False

class Test_Install_First_Apply_Tur_Moto(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # 在所有用例执行之前运行的
        print('我是setUpclass，我位于所有用例的开始（只执行一次）')
        adb_connect(devices_info_moto['udid'])     # 连接wifi调试
        huanxing_screen(devices_info_moto['udid']) # 唤醒屏幕
        #sildes(devices_info_moto['udid'], 360, 1400, 360, 1300, 50)          # adb向上滑屏
        uninstall_app(devices_info_moto['udid'], devices_info_moto['appPackage'])  # 预先卸载app包
        appium_start('127.0.0.1', port_moto)  # 启动appium服务

    def setUp(self):
        '''每条testcase执行前初始化'''
        print('testcase setUp')
        self.driver = devices_object_moto.init_devices(port_moto, devices_info_moto)
        # 设置隐式等待为 10s
        self.driver.implicitly_wait(10)
    def test_install_login(self):
        '''【turrant-android-MOTO】test_install_login-授权,登录-正案例'''
        shouquan_moto(self.driver)
        time.sleep(3)
        input = self.driver.find_element_by_id('com.turrant:id/phone')
        input.send_keys('8686860000')
        input2 = self.driver.find_element_by_id('com.turrant:id/code')
        input2.send_keys('5555')
        self.driver.find_element_by_id('com.turrant:id/login_btn').click()
    def test_install_frist_apply(self):
        '''【turrant-android-MOTO】test_install_first_apply-授权，进件5页面，检查数据抓取正案例'''
        shouquan_moto(self.driver)
        time.sleep(3)
        registNo=str(random.randint(7000000000,9999999999)) #10位随机数作为手机号
        print(registNo)
        self.driver.find_element_by_id('com.turrant:id/phone').send_keys(registNo)
        time.sleep(1)
        code = compute_code(registNo)
        self.driver.find_element_by_id('com.turrant:id/code').send_keys(code)
        self.driver.find_element_by_id('com.turrant:id/login_btn').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('com.turrant:id/loan_btn').click()  # step1点击申请贷款按钮,进入实名认证页面
        self.driver.find_element_by_xpath(xp1).send_keys('wang shuang')
        self.driver.find_element_by_xpath(xp2).send_keys('test')
        self.driver.find_element_by_xpath(xp3).send_keys('android')
        self.driver.find_element_by_xpath(xp4).click()
        time.sleep(5)
        self.driver.find_element_by_id("com.turrant:id/textView2").click()#点击ok
        self.driver.find_element_by_xpath(xp5).click()                    #点击education
        time.sleep(3)
        self.driver.find_element_by_id('com.turrant:id/textView2').click()#点击ok
        time.sleep(3)
        self.driver.find_element_by_xpath(xp6).click()     #marital status婚姻状况
        time.sleep(3)
        self.driver.find_element_by_id('com.turrant:id/textView2').click()#点击ok
        swipeup(self.driver,1000)
        self.driver.implicitly_wait(10)
        curtNo=certlist()
        self.driver.find_element_by_xpath(xp7).send_keys('wang123QQ@gmail.com')  #email
        self.driver.find_element_by_xpath(xp8).send_keys(curtNo[0])  #A卡
        self.driver.find_element_by_xpath(xp9).send_keys(curtNo[1])  #pan卡
        self.driver.find_element_by_xpath(xp10).click()  # 选择语言
        time.sleep(3)
        self.driver.find_element_by_id('com.turrant:id/textView2').click()
        time.sleep(3)
        self.driver.find_element_by_xpath(xp11).click()  #step2点击下一步,进入kyc页面
        time.sleep(3)
        self.driver.find_element_by_id('com.turrant:id/card_1').click()
        self.driver.find_element_by_id('com.turrant:id/tt_select_album').click()
        self.driver.find_element_by_xpath(xp12).click()
        self.driver.find_element_by_xpath(xp13).click()
        self.driver.find_element_by_id('com.turrant:id/card_2').click()
        self.driver.find_element_by_id('com.turrant:id/tt_select_album').click()
        self.driver.find_element_by_xpath(xp12).click()
        self.driver.find_element_by_xpath(xp13).click()
        self.driver.find_element_by_id('com.turrant:id/card_3').click()
        self.driver.find_element_by_id('com.turrant:id/tt_select_album').click()
        self.driver.find_element_by_xpath(xp12).click()
        self.driver.find_element_by_xpath(xp13).click()
        self.driver.find_element_by_id('com.turrant:id/card_4').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.oppo.camera:id/shutter_button').click()#点击拍照
        time.sleep(3)
        self.driver.find_element_by_id('com.oppo.camera:id/done_button').click() #点击确认
        time.sleep(3)
        self.driver.find_element_by_id('com.turrant:id/next').click() #step3点击下一步，进入家庭地址信息页面
        time.sleep(5)
        self.driver.find_element_by_xpath(xp14).send_keys('123456789')
        self.driver.find_element_by_xpath(xp15).send_keys('this is home address')
        self.driver.find_element_by_xpath(xp16).click()
        time.sleep(3)
        self.driver.find_element_by_id(id17).click()
        self.driver.find_element_by_xpath(xp18).click()
        time.sleep(3)
        self.driver.find_element_by_id(id19).click()
        self.driver.find_element_by_id('com.turrant:id/next').click()#step4点击下一步,进入工作信息证明页面
        time.sleep(5)
        self.driver.find_element_by_xpath(xp20).click()
        self.driver.find_element_by_id(id21).click()
        self.driver.find_element_by_xpath(xp22).send_keys('This Is Company Name')
        self.driver.find_element_by_xpath(xp23).click()
        self.driver.find_element_by_id(id24).click()
        self.driver.find_element_by_xpath(xp25).click()
        self.driver.find_element_by_id(id26).click()
        self.driver.find_element_by_id(id27).click()
        self.driver.find_element_by_id(id28).click()
        self.driver.find_element_by_id(id29).click()
        self.driver.find_element_by_xpath(xp30).click()
        self.driver.find_element_by_xpath(xp31).click()
        self.driver.find_element_by_id(id32).click()
        self.driver.find_element_by_id(id33).click()
        self.driver.find_element_by_xpath(xp34).click()
        self.driver.find_element_by_xpath(xp35).click()
        self.driver.find_element_by_id('com.turrant:id/next').click()  #step5点击下一步，进入联系人信息页面
        time.sleep(5)
        self.driver.find_element_by_id(id36).click()
        self.driver.find_element_by_id(id37).click()
        self.driver.find_element_by_xpath(xp38).send_keys('test android one')
        self.driver.find_element_by_xpath(xp39).send_keys('7474666222')
        self.driver.find_element_by_id(id40).click()
        time.sleep(1)
        self.driver.swipe(360, 1400, 360, 1300, 1000)
        time.sleep(1)
        self.driver.find_element_by_id('com.turrant:id/textView2').click() #点击ok
        self.driver.find_element_by_xpath(xp42).send_keys('test android two')
        self.driver.find_element_by_xpath(xp43).send_keys('7474666333')
        swipeup(self.driver,1000)
        self.driver.find_element_by_id('com.turrant:id/next').click() #点击提交申请
        time.sleep(30)
        self.driver.find_element_by_id('com.turrant:id/bind_bank').click() #提交成功后，点击ok按钮
        time.sleep(5)
        self.driver.find_element_by_id('com.turrant:id/tv_title').is_displayed()#检查是否被拒绝
        grab_data=cx_grab_data(registNo)
        for i in range(len(grab_data)):
            self.assertIsNotNone(grab_data[i])
        logout(self.driver)
    def tearDown(self):
        self.driver.quit()
        print("testcase done")
    @classmethod
    def tearDownClass(cls):  # 在所有用例都执行完之后运行的
        adb_disconnect(devices_info_moto['udid'])
        appium_stop(port_moto)
        print('我是tearDownClass，我位于多有用例运行的结束（只执行一次）')

if __name__ == '__main__':
    unittest.main()