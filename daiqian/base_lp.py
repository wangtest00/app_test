import datetime
import random
import string


#短信验证码，默认手机号后4位单个+5后取个位数，在逆序排列。注意非中国手机号规则.现在实际规则改为手机号后6位。。。没区别
def compute_code(m):
    m=m[-4:]
    x1=str(int(m[0])+5)
    x2=str(int(m[1])+5)
    x3=str(int(m[2])+5)
    x4=str(int(m[3])+5)
    x=x4[-1:]+x3[-1:]+x2[-1:]+x1[-1:]
    return x