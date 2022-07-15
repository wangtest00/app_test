from app.initDevices import *


inter_db = 'mex_pdl_loan'
prodNo = '25002400'#多期50121401
appNo = '201'
appName = 'LanaPlus'
# applist={'201':'LanaPlus','202':'FeriaRapida'}
# appName=applist[appNo]

port_hongmi = 4736  # appium和driver端口号
devices_object_hongmi = InitDevices(devices_path+'/devices_lp.yaml','hongmi')
devices_info_hongmi = devices_object_hongmi.read_devices()

CONFIGS = {
    'mex_pdl_loan': {'host':'192.168.0.60','port':3306, 'user': 'cs_wangs','password': 'cs_wangs!qw####','database': 'mex_pdl_loan'},
    'mex_new_point': {'host':'192.168.0.60','port':3306, 'user': 'cs_wangs','password': 'cs_wangs!qw####','database': 'new_point'}
}
