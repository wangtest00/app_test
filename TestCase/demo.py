from os import popen
# 在popen里放入需要执行的命令即可 这里我写的是ipconfig命令
text = popen("ipconfig").read()
print(text)