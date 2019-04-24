'''1. 对xampp中的apache日志文件（即所有.log结尾的文件）进行读取，
筛选出其中的错误信息(内容含error)，并全部输出到另一个文件new.log中。'''
import glob
f=glob.glob(r"D:\centos\xampp\apache\logs\*.log")
print(f)
file=open(r"D:\\centos\\xampp\\apache\\logs\\error.log",mode="a+")
file.seek(0)
content=file.readlines()
if content.index("error"):
    print(content)
