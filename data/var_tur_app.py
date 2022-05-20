from app.initDevices import *

inter_db='manage_need_loan'
prodNo='20150801'#duoqi50121401
applist={'104':'Turrant','102':'CashTM'}
appNo='104'
appName=applist[appNo]

port_oppo = 4723  # appium和driver端口号
devices_object_oppo = InitDevices(devices_path+'/devices.yaml', 'oppo')
devices_info_oppo = devices_object_oppo.read_devices()
port_moto = 4725
devices_object_moto = InitDevices(devices_path+'/devices.yaml', 'moto')
devices_info_moto = devices_object_moto.read_devices()
port_hongmi = 4727
devices_object_hongmi = InitDevices(devices_path+'/devices.yaml', 'hongmi')
devices_info_hongmi = devices_object_hongmi.read_devices()
print(devices_info_oppo)
CONFIGS = {
    'mex_pdl_loan': {'host':'192.168.0.60','port':3306, 'user': 'cs_wangs','password': 'cs_wangs!qw####','database': 'mex_pdl_loan'},
    'manage_need_loan': {'host':'13.235.214.155','port':3306, 'user': 'cs_wangs','password': 'cs_wangs!qw####','database': 'manage_need_loan'},
    'new_point': {'host':'13.235.214.155','port':3306, 'user': 'cs_wangs','password': 'cs_wangs!qw####','database': 'new_point'},
    'india_tez_loan': {'host':'172.21.0.244','port':3306, 'user': 'cs_wangs','password': 'cs_wangs!qw####','database': 'india_tez_loan'}
}
