import random,string,time,datetime
from data.var_lp import *
from dataBase.dataBase_Lp import *

def certlist():
    st=''
    for j in range(4):  #生成5个随机英文大写字母
        st+=random.choice(string.ascii_uppercase)
    num = str(random.randint(1000, 9999))
    Curp=st+"990519MM"+st+"V8"
    return Curp

 #退出登录
def logout(driver):
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[1]").click()
    time.sleep(3)
    driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="Abandonar"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//android.widget.Button[@content-desc="Confirme"]').click()
