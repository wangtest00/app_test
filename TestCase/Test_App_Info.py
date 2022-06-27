import csv,time,string
from os import popen
from data.commonPath import *
from data.var_turrant import *

class App(object):
    def __init__(self):
        self.content=""
        self.startTime=0

    def launchApp(self,udid,packageName,appActivity):
        cmd='adb -s '+udid+' shell am start -W -n '+packageName+'/'+appActivity
        self.content=popen(cmd).read()
        #print('launchApp响应=',self.content)

    def stopApp(self):
        cmd='adb shell input keyevent 3' #发送一个keyevent事件，3代表点击手机上的“back”键，构造热启动
        self.content=popen(cmd).read()
        #print('stopApp响应=',self.content)
    def forceStopApp(self,packageName):
        cmd='adb shell am force-stop '+packageName#强制停止   ,comment停止后再次启动就是冷启动了
        self.content=popen(cmd).read()
        #print('stopApp响应=',self.content)
    def getLaunchedTime(self):
        data=self.content.split('\n')
        for line in data:
            if 'TotalTime' in line:
                self.startTime=line.split(':')[1]
                break
        return self.startTime

class Controller(object):
    def __init__(self,count):
        self.app=App()
        self.counter=count
        self.alldata=[('timestamp','elapsedtime')]
    def testProcess(self,udid,packageName,appActivity):
        self.app.launchApp(udid,packageName,appActivity)
        time.sleep(5)
        elpasedtime=self.app.getLaunchedTime()
        self.app.stopApp()
        time.sleep(3)
        currentTime=self.getCurrentTime()
        self.alldata.append((currentTime,elpasedtime))
        #print(self.alldata)
    def run(self,udid,packageName,appActivity):
        while self.counter>0:
            self.testProcess(udid,packageName,appActivity)
            self.counter=self.counter-1
    def getCurrentTime(self):
        currentTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        return currentTime
    def saveDataToCSV(self):
        csvfile=open(report_path+'\\startTime2.csv','w')
        writer=csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()

class ControllerForCpu(object):
    def __init__(self,count):
        self.counter=count
        self.alldata=[('timestamp','cpustatus')]
    def testProcess(self,udid,packageName):
        result=popen('adb -s '+udid+' shell dumpsys cpuinfo | findstr '+packageName).read()
        print(result)
        cpuValue=result.split('%')[0]
        currentTime=self.getCurrentTime()
        self.alldata.append((currentTime,cpuValue))
    def run(self,udid,packageName):
        while self.counter>0:
            self.testProcess(udid,packageName)
            self.counter=self.counter-1
            time.sleep(3)
    def getCurrentTime(self):
        currentTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        return currentTime
    def saveDataToCSV(self):
        csvfile=open(report_path+'\\cpustatus.csv','w')
        writer=csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()

class ControllerForMeminfo(object): #内存
    def __init__(self,count):
        self.counter=count
        self.alldata=[('timestamp','cpustatus','Activities')]
    def testProcess(self,udid,packageName):
        result=popen('adb -s '+udid+' shell dumpsys meminfo '+packageName).read()
        data=result.split('\n')
        #print(data)
        if 'No process found for: '+packageName in data:
            print("app进程未开启")
            currentTime = self.getCurrentTime()
            self.alldata.append((currentTime, 'None'))
        else:
            for line in data:
                if 'TOTAL PSS' in line:
                    totalPSS=line.split(':')[1]
                    #print(totalPSS[:-21])
                elif 'Activities' in line:
                    Activities=line.split(':')[2]
                   # print(Activities)
                else:
                    pass
            currentTime=self.getCurrentTime()
            self.alldata.append((currentTime,totalPSS[:-21],Activities))
    def run(self,udid,packageName):
        while self.counter>0:
            self.testProcess(udid,packageName)
            self.counter=self.counter-1
            time.sleep(3)
    def getCurrentTime(self):
        currentTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        return currentTime
    def saveDataToCSV(self):
        csvfile=open(report_path+'\\meninfo.csv','w')
        writer=csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()

def get_Cpu(count,udid,packageName):
    controller = ControllerForCpu(count)
    controller.run(udid,packageName)
    controller.saveDataToCSV()

def get_StartTime(count,udid,packageName,appActivity):
    controller = Controller(count)
    controller.run(udid,packageName,appActivity)
    controller.saveDataToCSV()

def get_Meminfo(count,udid,packageName):
    controller = ControllerForMeminfo(count)
    controller.run(udid,packageName)
    controller.saveDataToCSV()

def get_Four_info(count,udid,packageName,appActivity):
    get_StartTime(count, udid, packageName, appActivity)
    get_Cpu(count, udid, packageName)
    get_Meminfo(count, udid, packageName)

if __name__ == '__main__':
    get_Four_info(1,devices_info_tur['udid'],devices_info_tur['appPackage'],devices_info_tur['appActivity'])
