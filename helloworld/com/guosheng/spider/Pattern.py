import re
#正则表达式,sub替换操作
b = "chuanli2dfl88"
c = re.sub("\d","_",b)
print(c)
p = re.compile("\D",re.S)
print(p.sub("_",b))
##r的效果，r在正则表达式中能够忽略转义字符带来的影响，.默认情况下是匹配不到\n的，所以需要使用dotall方式
print(r"a\nb" == "a\\nb")
print(re.findall(r"a\nb","a\\nb"))

print(re.findall(r"a.*bc","a\nbc",re.DOTALL))
print(re.findall(r"a(.*)bc","a\nbc",re.DOTALL))#加上括号，返回的是括号里面匹配到的内容