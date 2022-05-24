# 初始化设备
from appium import webdriver
import yaml
from logs.outputLog import OutputLog
from app.appium_adb import *
from data.common_path_tur import *

class InitDevices:
    def __init__(self, file_name, device_name):
        self.file_name = file_name
        self.device_name = device_name
    def read_devices(self):
        """
        获取设备信息
        :return:
        """
        try:
            OutputLog.output_log().debug("尝试获取设备信息")
            with open(self.file_name, 'r', encoding='utf-8') as f:
                all_devices = yaml.safe_load(f.read())
        except IOError:
            OutputLog.output_log().error("设备文件读取错误")
        else:
            msg = str(all_devices[self.device_name])
            OutputLog.output_log().debug(msg)
            return all_devices[self.device_name]
    def init_devices(self,port,device_info):
        """
        初始化设备
        :param device_info:
        :return:
        """
        return webdriver.Remote("http://127.0.0.1:"+str(port)+"/wd/hub", device_info)


# if __name__ == "__main__":
#     OutputLog.output_log().debug("==============开始测试，连接手机==============")
#     devices_object = InitDevices(devices_path+'/devices_tur.yaml', 'oppo')
#     devices_info = devices_object.read_devices()
#     print(devices_info)
#     devices = devices_object.init_devices(4723,devices_info)
#     # OutputLog.output_log().debug("连接成功")  # 连接成功，开始找元素