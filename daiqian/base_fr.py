from dataBase.dataBase_Fr import *
from data.var_fr import *

#短信验证码，默认手机号后4位单个+5后取个位数，在逆序排列。注意非中国手机号规则.现在实际规则改为手机号后6位。。。没区别
def compute_code(m):
    m=m[-4:]
    x1=str(int(m[0])+5)
    x2=str(int(m[1])+5)
    x3=str(int(m[2])+5)
    x4=str(int(m[3])+5)
    x=x4[-1:]+x3[-1:]+x2[-1:]+x1[-1:]
    return x
def fk_phone():
    sql='''
    select  b.cust_no,count(1) as loan_cnt, c.REGIST_NO from (select  a.cust_no from
    lo_loan_dtl a
    WHERE
	a.BEFORE_STAT = '10260005'
    AND a.AFTER_STAT = '10270005'
    and date(a.INST_TIME)<date(now())
    GROUP BY a.cust_no
    HAVING count(1) =1
    )a INNER JOIN lo_loan_dtl b on a.cust_no=b.cust_no inner join cu_cust_reg_dtl c on b.cust_no=c.cust_no 
    INNER JOIN cu_cust_pwd_dtl d on c.REGIST_NO=d.REGIST_NO
    where c.APP_NO='202'
    group by  b.cust_no
    HAVING loan_cnt=1
    order by b.INST_TIME desc limit 1;'''
    result = DataBase(inter_db).get_one(sql)
    print(result[2])
    return result[2]
def hk_phone():
    sql='''
    select a.REGIST_NO
    from cu_cust_reg_dtl a 
    LEFT JOIN lo_loan_dtl b
    on a.CUST_NO=b.CUST_NO
    where b.AFTER_STAT='10270002'
    and a.APP_NO='202'
    ORDER BY b.INST_TIME desc limit 1;'''
    result = DataBase(inter_db).get_one(sql)
    #print(result[0])
    return result[0]

if __name__ == '__main__':
    hk_phone()
