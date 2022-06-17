from app.initDevices import *
from data.commonPath import  *


port_tiktok = 4733  # appium和driver端口号
devices_object_tiktok = InitDevices(devices_path+'/devices_third.yaml', 'tiktok')
devices_info_tiktok = devices_object_tiktok.read_devices()

port_moutai = 4734  # appium和driver端口号
devices_object_moutai = InitDevices(devices_path+'/devices_third.yaml', 'moutai')
devices_info_moutai = devices_object_moutai.read_devices()