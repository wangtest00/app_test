from app.initDevices import *
from data.common_path import *


port_oppo = 4733  # appium和driver端口号
devices_object_oppo = InitDevices(devices_path+'/devices_tiktok.yaml', 'oppo')
devices_info_oppo = devices_object_oppo.read_devices()

