from appium import webdriver
import unittest,requests,time
from daiqian.base_lp import *
from daiqian.auth_lp import *
from data.var_lp import *
from app.grab_data_lp import *
from app.appium_adb import *
from app.swipe_test import *
from app.initDevices import *
from data.common_path import *
import warnings
from public.change_shurukaung import *
from data.path_lp import *


class Test_Install_Login_Lp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # 在所有用例执行之前运行的
        print('我是setUpclass，我位于所有用例的开始')
        adb_connect(devices_info_hongmi['udid'])     # 连接wifi调试
        huanxing_screen(devices_info_hongmi['udid']) # 唤醒屏幕
        sildes(devices_info_hongmi['udid'], 360, 1400, 360, 500, 1000)          # adb向上滑屏
        uninstall_app(devices_info_hongmi['udid'], devices_info_hongmi['appPackage'])  # 预先卸载app包
        appium_start('127.0.0.1', port_hongmi)  # 启动appium服务

    def setUp(self):
        '''每条testcase执行前初始化'''
        print('testcase setUp')
        self.driver = devices_object_hongmi.init_devices(port_hongmi, devices_info_hongmi)
        # 设置隐式等待为 10s,一旦设置了隐式等待，它则会在整个Web Driver对象的实例声明周期中。
        self.driver.implicitly_wait(10)

    def test_install_login(self):
        '''【LanaPlus-android-HongMi】test_install_login-新用户登录-设置密码,授权-正案例'''
        # 读取设备登录google play的手机号
        self.driver.find_element_by_id("com.google.android.gms:id/cancel").click()  # 点击以上都不是
        registNo = str(random.randint(1000000000,1999999999))  # 10位随机数作为手机号
        code = compute_code(registNo)  # 计算验证码
        mima = "123456"  # 密码
        change_shuru(self.driver, xp1, registNo)
        time.sleep(3)
        self.driver.find_element_by_xpath(xp2).click()  # 点击注册按钮
        time.sleep(3)
        change_shuru(self.driver, xp3, code)  # 输入验证码
        time.sleep(3)
        change_shuru(self.driver, xp4, mima)  # 输入密码
        time.sleep(3)
        change_shuru(self.driver, xp5, mima)  # 再次输入密码
        time.sleep(3)
        shouquan_hongmi(self.driver)
        time.sleep(3)
        self.assertTrue(self.driver.find_element_by_xpath(xp6).is_displayed())  # 判断进入了申请页面
    def test_install_login_jinzhi_shouquan(self):
        '''【LanaPlus-android-HongMi】test_install_login_jinzhi_shouquan-新用户登录-设置密码,禁止授权-正案例'''
        # 读取设备登录google play的手机号
        self.driver.find_element_by_id("com.google.android.gms:id/cancel").click()  # 点击以上都不是
        registNo = str(random.randint(1000000000, 1999999999))  # 10位随机数作为手机号
        code = compute_code(registNo)  # 计算验证码
        mima = "123456"  # 密码
        change_shuru(self.driver, xp1, registNo)
        time.sleep(3)
        self.driver.find_element_by_xpath(xp2).click()  # 注册按钮
        time.sleep(3)
        change_shuru(self.driver, xp3, code)  # 输入验证码
        time.sleep(3)
        change_shuru(self.driver, xp4, mima)  # 输入密码
        time.sleep(3)
        change_shuru(self.driver, xp5, mima)  # 再次输入密码
        time.sleep(8)
        self.driver.find_element_by_xpath('//android.view.View[@content-desc="Aceptar y continuar"]').click()
        time.sleep(3)
        self.driver.find_element_by_id("com.lbe.security.miui:id/permission_deny_button").click()
        time.sleep(3)
        self.driver.find_element_by_id("com.lbe.security.miui:id/permission_deny_button").click()
        time.sleep(3)
        self.driver.find_element_by_id("com.lbe.security.miui:id/permission_deny_button").click()
        time.sleep(3)
        self.driver.find_element_by_id("com.lbe.security.miui:id/permission_deny_button_1").click()
        time.sleep(3)
        self.driver.find_element_by_id("com.lbe.security.miui:id/permission_deny_button_1").click()
        time.sleep(3)
        self.driver.find_element_by_id("com.lbe.security.miui:id/permission_deny_and_dont_ask_again_button").click()  # 拒绝且不再询问
        time.sleep(3)
        self.driver.find_element_by_id("com.lbe.security.miui:id/permission_deny_and_dont_ask_again_button").click()  # 拒绝且不再询问
        time.sleep(3)
        self.driver.find_element_by_id("com.lbe.security.miui:id/permission_deny_and_dont_ask_again_button").click()  # 拒绝且不再询问
        time.sleep(3)
        self.driver.find_element_by_id("com.lbe.security.miui:id/permission_deny_and_dont_ask_again_button").click()  # 拒绝且不再询问
        time.sleep(3)
        self.driver.find_element_by_id("com.lbe.security.miui:id/permission_deny_and_dont_ask_again_button").click()  # 拒绝且不再询问
        time.sleep(3)
        self.assertTrue(self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="Confirmar"]').is_displayed())
    def test_install_login_first_apply(self):
        '''【LanaPlus-android-HongMi】test_install_login_first_apply-新客登录-设置密码，授权，进件4页面-绑卡，检查数据抓取正案例'''
        # 读取设备登录google play的手机号
        self.driver.find_element_by_id("com.google.android.gms:id/cancel").click()  # 点击以上都不是
        registNo = str(random.randint(1000000000,1999999999))  # 10位随机数作为手机号
        #registNo='8695333579'
        print(registNo)
        code = compute_code(registNo)  # 计算验证码
        mima = "123456"  # 密码
        postal = '11111' # 邮政编码
        bankNo = "138000000000000008"  # 银行卡
        change_shuru(self.driver, xp1, registNo)
        time.sleep(3)
        self.driver.find_element_by_xpath(xp2).click()  # 注册按钮
        time.sleep(3)
        change_shuru(self.driver, xp3, code)  # 输入验证码
        time.sleep(3)
        change_shuru(self.driver, xp4, mima)  # 输入密码
        time.sleep(3)
        change_shuru(self.driver, xp5, mima)  # 再次输入密码
        time.sleep(3)
        shouquan_hongmi(self.driver)  # 授权
        time.sleep(3)
        self.driver.find_element_by_xpath(xp6).click()   # step1点击申请贷款按钮
        time.sleep(3)
        change_shuru(self.driver, xp8, 'lll')  # 姓名
        change_shuru(self.driver, xp9, 'test')  # 父亲的姓
        change_shuru(self.driver, xp10, 'android')  # 母亲的姓
        self.driver.find_element_by_xpath(xp11).click()  # 出生日期
        self.driver.find_element_by_xpath(xp12).click()  # 点击ok
        self.driver.find_element_by_xpath(xp13).click()  # 性别
        self.driver.find_element_by_xpath(xp14).click()  # 点击ok
        self.driver.find_element_by_xpath(xp15).click()  # 婚姻状况
        self.driver.find_element_by_xpath(xp16).click()  # 点击ok
        time.sleep(3)
        Curp=certlist()
        swipeup(self.driver, 1000)
        change_shuru(self.driver, xp17, Curp)  # curp
        time.sleep(3)
        change_shuru(self.driver, xp18, 'this is Calle')  # 街道
        change_shuru(self.driver, xp19, 'this is Numero exterior')  # 室外号码
        change_shuru(self.driver, xp20, 'this is Colonia')  # 市郊
        change_shuru(self.driver, xp21, postal)  # 邮政编码
        change_shuru(self.driver, xp22, 'this is Delegaion o Municipio')  # 代表团或市政府
        swipeup(self.driver, 1000)
        self.driver.find_element_by_xpath(xp23).click()  # 州
        time.sleep(3)
        self.driver.find_element_by_xpath(xp24).click()  # 点击ok
        self.driver.find_element_by_xpath(xp25).click()  # 教育程度
        self.driver.find_element_by_xpath(xp26).click()  # 点击ok
        self.driver.find_element_by_xpath(xp27).click()  # step2点击下一步,进入kyc页面
        time.sleep(3)
        self.driver.find_element_by_xpath(xp28).click()
        self.driver.find_element_by_xpath(xp29).click()  # 点击确定
        self.driver.find_element_by_id(id30_hongmi).click()  # 拍照授权
        self.driver.find_element_by_xpath(xp31).click()  # 第一张拍照
        time.sleep(3)
        self.driver.find_element_by_xpath(xp32).click()
        self.driver.find_element_by_xpath(xp33).click()
        self.driver.find_element_by_xpath(xp34).click()  # 第二张拍照
        time.sleep(3)
        self.driver.find_element_by_xpath(xp35).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(xp36).click()
        self.driver.find_element_by_xpath(xp37).click()  # 切换摄像头
        self.driver.find_element_by_xpath(xp38).click()  # 第三张拍照
        time.sleep(3)
        self.driver.find_element_by_xpath(xp39).click()  # step3点击下一步，进入工作信息页面
        time.sleep(5)
        self.driver.find_element_by_xpath(xp40).click()  # 点击工作类型
        self.driver.find_element_by_xpath(xp41).click()  # 点击ok
        self.driver.find_element_by_xpath(xp42).click()  # 点击收入按钮
        self.driver.find_element_by_xpath(xp43).click()  # 点击ok
        self.driver.find_element_by_xpath(xp44).click()  # step4点击下一步,进入联系人页面
        time.sleep(5)
        self.driver.find_element_by_xpath(xp45).click()  # 第一个联系人关系
        self.driver.find_element_by_xpath(xp46).click()  # 点击ok
        self.driver.find_element_by_xpath(xp47).click()  # 点击通讯录图标
        self.driver.find_element_by_xpath(xp48).click()  # 选择对应的联系人电话信息
        time.sleep(3)
        self.driver.find_element_by_xpath(xp49).click()  # 第二个联系人关系
        self.driver.find_element_by_xpath(xp50).click()  # 点击ok
        self.driver.find_element_by_xpath(xp51).click()  # 点击通讯录图标
        self.driver.find_element_by_xpath(xp52).click()  # 选择对应的联系人电话信息
        time.sleep(3)
        self.driver.find_element_by_xpath(xp53).click()  # 点击提交按钮
        time.sleep(5)
        self.driver.find_element_by_xpath(xp54).click()  # 评三颗星星
        self.driver.find_element_by_xpath(xp55).click()  # 点击ok
        self.driver.find_element_by_xpath(xp56).click()  # 取消去反馈
        time.sleep(4)
        # self.driver.find_element_by_xpath(xp57).click()  # 点击继续进入银行卡页面
        # time.sleep(3)
        # self.driver.find_element_by_xpath(xp58).click()  # 点击银行卡机构
        # self.driver.find_element_by_xpath(xp59).click()  # 点击ok
        # time.sleep(3)
        # change_shuru(self.driver, xp60, bankNo)  # 输入银行卡卡号
        # time.sleep(3)
        # self.driver.find_element_by_xpath(xp58).click()
        # self.driver.find_element_by_xpath(xp61).click()
        # time.sleep(2)
        # self.driver.find_element_by_xpath(xp62).click()  # 点击提交
        # time.sleep(3)
        # self.driver.find_element_by_xpath(xp63).click()  # 点击确定
        # time.sleep(3)
        # self.driver.find_element_by_xpath(xp64).click()  # 待审批--填写邮箱
        # time.sleep(3)
        # self.driver.find_element_by_xpath(xp65).click() # 邮箱入口
        # self.driver.find_element_by_id('com.google.android.gms:id/cancel').click() # 点击以上都不是
        # change_shuru(self.driver, xp66, "test@gmail.com")  # 填写邮箱
        # time.sleep(3)
        # self.driver.find_element_by_xpath(xp67).click()  # 点击确认
        # time.sleep(3)
        # self.driver.find_element_by_xpath(xp68).click()  # 点击返回按钮
        # 校验抓取的5个数据不为空
        grab_data = cx_grab_data(registNo)
        for i in range(len(grab_data)):
            self.assertIsNotNone(grab_data[i])
        logout(self.driver)  # 退出登录
    def test_install_login_fuke(self):
        '''【LanaPlus-android-HongMi】test_install_login_fuke-复客登录-一键复贷，检查数据抓取正案例'''
        # 读取设备登录google play的手机号
        self.driver.find_element_by_id("com.google.android.gms:id/cancel").click()  # 点击以上都不是
        registNo = fk_phone()  # 复客手机号
        mima = "123456"  # 密码
        change_shuru(self.driver, xp1, registNo)
        time.sleep(3)
        self.driver.find_element_by_xpath(xp2).click()  # 注册按钮
        time.sleep(3)
        change_shuru(self.driver,xp3, mima)  # 输入密码
        time.sleep(3)
        shouquan_hongmi(self.driver)  # 授权
        time.sleep(3)
        # self.driver.find_element_by_xpath(xp93).click()  # 点击下一笔贷款倾向性选择，提高贷款金额
        # self.driver.find_element_by_xpath(xp94).click()  # 点击确定
        # self.driver.find_element_by_xpath(xp95).click()  # 点击ok
        # time.sleep(3)
        self.driver.find_element_by_xpath(xp6).click()  # 点击申请贷款
        time.sleep(15)
        self.driver.find_element_by_xpath(xp54).click()  # 评三颗星星
        self.driver.find_element_by_xpath(xp55).click()  # 点击ok
        self.driver.find_element_by_xpath(xp56).click()  # 取消去反馈
        time.sleep(3)
        # 校验抓取的5个数据不为空
        grab_data = cx_grab_data(registNo)
        for i in range(len(grab_data)):
            self.assertIsNotNone(grab_data[i])
        #退出登录
        logout(self.driver)
    def test_install_login_huankuan(self):
        '''【LanaPlus-android-HongMi】test_install_login_huankuan-还款用户登录-日历事件写入-申请还款正案例'''
        # 读取设备登录google play的手机号
        self.driver.find_element_by_id("com.google.android.gms:id/cancel").click()  # 点击以上都不是
        registNo = hk_phone()  # 还款手机号
        mima = "123456"  # 密码
        change_shuru(self.driver, xp1, registNo)
        time.sleep(3)
        self.driver.find_element_by_xpath(xp2).click()  # 注册按钮
        time.sleep(3)
        change_shuru(self.driver, xp3, mima)  # 输入密码
        time.sleep(3)
        shouquan_hongmi(self.driver)  # 授权
        # # 日历事件的写入
        # self.driver.find_element_by_xpath(xp67).click()  # 点击去写入日历事件
        # self.driver.find_element_by_xpath(xp68).click()  # 点击确定
        # time.sleep(3)
        # # 点击还款账单详情
        # self.driver.find_element_by_xpath(xp70).click()
        # 获取还款方式
        self.driver.find_element_by_xpath(xp71).click()
        time.sleep(3)
        # 默认选择STP还款
        self.driver.find_element_by_xpath(xp73).click()
        time.sleep(3)
        #判断进入stp还款信息页面
        self.assertTrue(self.driver.find_element_by_xpath(xp74).is_displayed())
    # def test_install_login_quxiaorili(self):
    #     '''【LanaPlus-android-HongMi】test_install_login_quxiaorili-还款用户登录-取消日历事件写入-正案例'''
    #     # 读取设备登录google play的手机号
    #     self.driver.find_element_by_id("com.google.android.gms:id/cancel").click()  # 点击以上都不是
    #     registNo = hk_phone()  # 还款手机号
    #     mima = "123456"  # 密码
    #     change_shuru(self.driver, xp1, registNo)
    #     time.sleep(3)
    #     self.driver.find_element_by_xpath(xp2).click()  # 注册按钮
    #     time.sleep(3)
    #     change_shuru(self.driver, xp3, mima)  # 输入密码
    #     time.sleep(3)
    #     # 日历事件的写入
    #     self.driver.find_element_by_xpath(xp67).click()  # 点击去写入日历事件
    #     self.driver.find_element_by_xpath(xp69).click()  # 点击取消
    #     self.driver.find_element_by_id('android:id/button1').click()  # 点击确定
    #     shouquan_hongmi(self.driver)  # 授权
    #     time.sleep(3)
    def test_install_login_fankui(self):
        '''【LanaPlus-android-HongMi】test_install_login_fankui-新用户登录-反馈信息-正案例'''
        # 读取设备登录google play的手机号
        self.driver.find_element_by_id("com.google.android.gms:id/cancel").click()  # 点击以上都不是
        registNo = str(random.randint(1000000000, 1999999999))  # 10位随机数作为手机号
        code = compute_code(registNo)  # 计算验证码
        mima = "123456"  # 密码
        detalls = "testtest"
        change_shuru(self.driver, xp1, registNo)
        time.sleep(3)
        self.driver.find_element_by_xpath(xp2).click()  # 点击注册按钮
        time.sleep(3)
        change_shuru(self.driver, xp3, code)  # 输入验证码
        time.sleep(3)
        change_shuru(self.driver, xp4, mima)  # 输入密码
        time.sleep(3)
        change_shuru(self.driver, xp5, mima)  # 再次输入密码
        time.sleep(3)
        shouquan_hongmi(self.driver)
        time.sleep(3)
        self.driver.find_element_by_xpath(xp75).click()  # 点击反馈图标
        self.driver.find_element_by_xpath(xp76).click()
        self.driver.find_element_by_xpath(xp77).click()

        # change_shuru(self.driver, xp81, detalls)  # 输入描述
        # swipeup(self.driver, 1000)

        self.driver.find_element_by_xpath(xp78).click()  # 点击反馈问题
        self.driver.find_element_by_xpath(xp79).click()  # 点击ok
        self.driver.find_element_by_xpath(xp80).click()
        self.driver.find_element_by_xpath(xp82).click()  # 选择第一个添加图片
        self.driver.find_element_by_xpath(xp83).click()  # 去相册选择
        self.driver.find_element_by_xpath(xp84).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(xp85).click()  # 选择第二个添加图片
        self.driver.find_element_by_xpath(xp83).click()  # 去相册选择
        self.driver.find_element_by_xpath(xp86).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(xp87).click()  # 点击反馈按钮
        self.driver.find_element_by_xpath(xp88).click()  # 点击ok
    def test_install_login_chexiao(self):
        '''【LanaPlus-android-HongMi】test_install_login_chexiao-撤销用户登录--重新进件正案例'''
        # 读取设备登录google play的手机号
        self.driver.find_element_by_id("com.google.android.gms:id/cancel").click()  # 点击以上都不是
        registNo = cx_phone()  # 撤销用户手机号
        mima = "123456"  # 密码
        change_shuru(self.driver, xp1, registNo)
        time.sleep(3)
        self.driver.find_element_by_xpath(xp2).click()  # 注册按钮
        time.sleep(3)
        change_shuru(self.driver, xp3, mima)  # 输入密码
        time.sleep(3)
        shouquan_hongmi(self.driver)  # 授权
        time.sleep(3)
        self.driver.find_element_by_xpath(xp89).click()  # 点击重新申请贷款按钮
        # self.driver.find_element_by_xpath(xp6).click()
        self.driver.find_element_by_xpath(xp89).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(xp89).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(xp89).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(xp89).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(xp54).click()  # 评分
        self.driver.find_element_by_xpath(xp55).click()
        self.driver.find_element_by_xpath(xp56).click()
    def tearDown(self):
        self.driver.quit()
        print("testcase done")

    @classmethod
    def tearDownClass(cls):  # 在所有用例都执行完之后运行的
        adb_disconnect(devices_info_hongmi['udid'])
        appium_stop(port_hongmi)
        print('我是tearDownClass，我位于所有用例运行的结束')

if __name__ == '__main__ ':
    unittest.main()