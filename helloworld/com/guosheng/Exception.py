'''
python异常都是error
'''
try:
    print(1/0)
except Exception as msg:
    print(msg)
else:
    print("3455")#没有发生异常的时候执行
finally:
    print("finally")
