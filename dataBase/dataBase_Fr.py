# coding:utf-8

import time
import pymysql
from data.var_fr import *
from public.date_calculate import *

class DataBase():
    def __init__(self,witchdb):
        self.connectDB(witchdb)
    def connectDB(self,witchdb):
        try:
            self.connect=pymysql.connect(user=CONFIGS[witchdb]['user'],password=CONFIGS[witchdb]['password'],host=CONFIGS[witchdb]['host'],
                                         database=CONFIGS[witchdb]['database'],port=CONFIGS[witchdb]['port'], charset="utf8")
            self.cur=self.connect.cursor()
        except pymysql.Error as e:
            print(e)
    def get_all(self, sql):
        try:
            self.cur.execute(sql)
            value = self.cur.fetchall()
            return value
        except Exception as e:
            print("查询全部结果异常：",e)
            return 0
    def get_one(self,sql):
        try:
            self.cur.execute(sql)
            value = self.cur.fetchone()
            return value
        except Exception as e:
            print("查询单个结果异常：",e)
            return 0
    def closeDB(self):
        self.cur.close()
        self.connect.close()
    def executeUpdateSql(self,sql):
        try:
            self.cur.execute(sql)
            self.connect.commit()
            print ("更新表字段成功",sql)
            self.closeDB()
        except Exception as e:
            print("更新异常：",e)
            return 0
    #调用mysql存储过程
    def call_proc(self,procName):
        try:
            self.cur.callproc(procName,args=("@o_stat",))
            self.connect.commit()
            print ("调用存储过程成功:",procName)
            #self.closeDB()
        except Exception as e:
            print("调用存储过程异常：",e)
            return 0
    def call_proc_args(self,procName,date):
        try:
            self.cur.callproc(procName,args=(date,"@o_stat"))
            self.connect.commit()
            print ("调用存储过程成功:",procName,date)
            #self.closeDB()
        except Exception as e:
            print("调用存储过程异常：",e)
            return 0
    def call_many_proc(self):
        proc=['proc_apr_loan_prod_sel','proc_apr_appr_all_user','proc_apr_appr_allocation_control','proc_apr_appr_allo_user_deal']
        for proc in proc:
            self.call_proc(proc)
        self.closeDB()
    #调用存储过程，执行日终批量，从日期1跑到日期2
    def call_daily_important_batch(self,date1,date2):
        sql="delete from sys_batch_log;"
        DataBase(tez_db).executeUpdateSql(sql)
        proc=['proc_sys_batch_log_start','proc_fin_ad_ovdu','proc_fin_ad_detail_dtl','proc_fin_ad_dtl','proc_lo_ovdu_dtl','proc_sys_batch_log_end']
        date=create_assist_date(date1,date2)
        print(date)
        for j in range(len(date)):
            for i in range(len(proc)):
                self.call_proc_args(proc[i],date[j])
                time.sleep(1)
        self.closeDB()


#loanAmt='{0:f}'.format(t[0])#decimal转字符串

if __name__ == '__main__':
    DataBase(inter_db).call_daily_important_batch('20220208','20220208')