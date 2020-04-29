'''
os模块
文件操作
'''
import  os
print(os.name)
print(os.listdir())
print(os.getcwd())#获取当前文件目录
os.remove("")#删除指定文件,
os.mkdir("")
os.path.isfile("")#判断是否是一个文件
os.path.getsize("")#获取文件大小
os.path.basename("")#获取文件名
os.system("java -version")#执行系统脚本命令