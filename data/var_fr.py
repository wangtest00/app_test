from app.initDevices import *
#__all__=['devices_info_2','devices_object_2']

# devices_object = InitDevices('../devices.yaml','oppo')
# devices_object_2=devices_object
# devices_info = devices_object.read_devices()
# devices_info_2=devices_info
# print('666',devices_info_2)

inter_db='mex_pdl_loan'
prodNo='25002400'#多期50121401
appNo='202'
appName='FeriaRapida'
# applist={'201':'LanaPlus','202':'FeriaRapida'}
# appName=applist[appNo]

port_vivo = 4733  # appium和driver端口号
devices_object_vivo = InitDevices(devices_path+'/devices_fr.yaml', 'vivo')
devices_info_vivo = devices_object_vivo.read_devices()

port_samsung = 4734  # appium和driver端口号
devices_object_samsung = InitDevices(devices_path+'/devices_fr.yaml','samsung')
devices_info_samsung = devices_object_samsung.read_devices()

port_hongmi = 4735  # appium和driver端口号
devices_object_hongmi = InitDevices(devices_path+'/devices_fr.yaml','hongmi')
devices_info_hongmi = devices_object_hongmi.read_devices()

CONFIGS = {
    'mex_pdl_loan': {'host':'192.168.0.60','port':3306, 'user': 'cs_wangs','password': 'cs_wangs!qw####','database': 'mex_pdl_loan'},
    'mex_new_point': {'host':'192.168.0.60','port':3306, 'user': 'cs_wangs','password': 'cs_wangs!qw####','database': 'new_point'}
}
