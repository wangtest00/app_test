from appium import webdriver
import unittest,os,time,requests
from daiqian.base_lp import *
from app.auth_tur import *
from data.var_tur_app import *
from app.grab_data import *
from app.appium_adb import *
from app.swipe_test import *
from app.initDevices import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

port = 4723  # appium和driver端口号
#增加重试连接次数
requests.DEFAULT_RETRIES = 5
#关闭多余的链接：requests使用了urllib3库，默认的http connection是keep-alive的，requests设置False关闭
s = requests.session()
s.keep_alive = False

class Test_Install_Login_Tur2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('我是setUpclass，我位于所有用例的开始')
        devices_object = InitDevices('../devices.yaml','oppo')
        devices_info = devices_object.read_devices()
        print(devices_info)
        adb_connect(devices_info['udid'])                      #连接wifi调试
        huanxing_screen(devices_info['udid'])                  #唤醒屏幕
        sildes(devices_info['udid'],360, 1400, 360, 1300, 50)  #adb向上滑屏
        uninstall_app(devices_info['udid'],devices_info['appPackage'])#预先卸载app包
        appium_start('127.0.0.1', port)                        #启动appium服务

    def setUp(self):
        '''每条testcase执行前初始化'''
        print('testcase setUp')
        devices_object = InitDevices('../devices.yaml', 'oppo')
        devices_info = devices_object.read_devices()
        self.driver=devices_object.init_devices(port, devices_info)
        #设置隐式等待为 10s,一旦设置了隐式等待，它则会在整个Web Driver对象的实例声明周期中。
        self.driver.implicitly_wait(10)
        swipeup(self.driver,1000)
    def test_jinzhi_shouquan(self):
        '''【turrant-android-OPPO】test_jinzhi_shouquan-禁止授权-正案例'''
        self.driver.find_element_by_id('com.turrant:id/agree').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.android.permissioncontroller:id/permission_deny_button').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.android.permissioncontroller:id/permission_deny_button').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.android.permissioncontroller:id/permission_deny_button').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.android.permissioncontroller:id/permission_deny_button').click()
        time.sleep(3)
        self.assertTrue(self.driver.find_element_by_id('com.turrant:id/tt_msg').is_displayed())
    def test_install_login(self):
        '''【turrant-android-OPPO】test_install_login-授权,登录-正案例'''
        shouquan_oppo(self.driver)
        time.sleep(3)
        input = self.driver.find_element_by_id('com.turrant:id/phone')
        input.send_keys('8686863333')
        input2 = self.driver.find_element_by_id('com.turrant:id/code')
        input2.send_keys('8888')
        self.driver.find_element_by_id('com.turrant:id/login_btn').click()
    def test_install_first_apply(self):
        '''【turrant-android-OPPO】test_install_first_apply-授权，进件5页面，检查数据抓取/埋点数据量-正案例'''
        shouquan_oppo(self.driver)
        time.sleep(3)
        registNo=str(random.randint(7000000000,9999999999)) #10位随机数作为手机号
        print(registNo)
        insert_white_list(registNo)
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
        # time.sleep(5)                                #工作信息附件证明
        # self.driver.find_element_by_id(id27).click()
        # time.sleep(5)
        # self.driver.find_element_by_id(id28).click()
        # self.driver.find_element_by_id(id29).click()
        # self.driver.find_element_by_xpath(xp30).click()
        # self.driver.find_element_by_xpath(xp31).click()
        # self.driver.find_element_by_id(id32).click()
        # self.driver.find_element_by_id(id33).click()
        # self.driver.find_element_by_xpath(xp34).click()
        # self.driver.find_element_by_xpath(xp35).click()
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
        #self.driver.find_element_by_id('com.turrant:id/tv_title').is_displayed()#检查是否被拒绝
        grab_data=cx_grab_data(registNo)
        for i in range(len(grab_data)):
            self.assertIsNotNone(grab_data[i])
        time.sleep(10)
        self.assertEqual(cx_point_track_dtl_new(registNo),'26')
        logout(self.driver)
    def tearDown(self):
        self.driver.quit()
        print("testcase done")
    @classmethod
    def tearDownClass(cls):
        devices_object = InitDevices('../devices.yaml', 'oppo')
        devices_info = devices_object.read_devices()
        adb_disconnect(devices_info['udid'])
        appium_stop(port)
        print('我是tearDownClass，我位于所有用例运行的结束')

# if __name__ == '__main__':
#     unittest.main()