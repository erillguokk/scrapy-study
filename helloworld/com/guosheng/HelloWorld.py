
'''
python中有Numberic类型：整型，浮点型，布尔型
'''
######基本类型整形、布尔型、字符串型、#####
print("helloworld")
a =10
str="slsjf"
flag = True
flag = None #表示一个特殊的空值
b="3456"
print(type(int(b)))#类型转换
import keyword
print(keyword.kwlist)
print("hello","world","yes")
print("%s"%b)
f=123.456
print("%.1f"%f)
s=input("请输入：")
print(s)
############运算符###############
print(10/3)
print(10//3)
print(2**3)#2的三次方
a,b=1,2#复制运算符
1 and 2 #逻辑运算符 and or not
#比较运算符<>标识不等于

##############逻辑判断与循环######################
age = input("请输入年龄：")
age = int(age)#强制类型转换
if(age<20):
    print("aa")
elif(age<40):
    print("bb")
else:
    print("cc")

i=0
sum = 0
while i<=100:
    sum+=i
    i+=1

for i in 1,2,3,4,5:
    print(i)

for i in range(1,10,2):#以步长为2来遍历1-10
    print(i)
for i in "abckdlf":
    print(i)
    for i in "abckdlf","flfj","flajfj":
        print(i)
        pass
else:print("循环完了")
###########九九乘法表#################
i = 1;
# while i<10:
#     j = 1
#     while(j<=i):
#         print("%d*%d=%d"%(i,j,i*j),end="\t")
#         if(i==j):
#             print()
#             pass
#         j += 1
#         pass
#     i+=1

for i in range(1,10):
    j=1
    for j in range(1,i+1):
        print("%d*%d=%d" % (i, j, i * j), end="\t")
        if(i==j):
            print()
            pass

############字符串###############
str = "abckderglu"
print(str[2])
print(str[-1])
print(str[::])#切片，起始索引，结束索引，步长 左闭右开
print(str[5:2:-1])#-代表是逆序
print(str[4::-1])
x = str.index("k")#找不到会抛出异常
y = str.rindex("k")
z = str.find("k")#找不到就是-1
print(str.count("a",0,4))#在0-4，左闭右开范围内 a出现的次数
print(str.split(" "))
str.upper()
str.title()
str.startswith("a")

#########列表对象##########
#python通过符号来标识各种数据结构
list = ["abcd",123,True,123.456]
print(list[::-2])
for i in list:
    print(i)
    pass
for i,v in enumerate(list):
    print(i,v)
    pass

list.append("cc")#增加元素
list.insert(2,"zz")
list2 = [1,2,4,"ddf"]
list.extend(list2)
list.remove("abcd")
list.pop(0)
del list[0]#删除元素
list.sort()

############元组对象#########
tuple = ("ab",True,1,22)#与列表相似，但是不能对元素进行修改，不可变
t =(2,)#是一个元素的元组
t =(1)#不是元组
t=(1,44,"aa")
print(t)
t[2][2] = "cc"
print(t)
#############字典######################
dict = {"a":100,"b":200}
print(dict["a"])
dict["c"]=300#key不可以重复，可以添加元素
print(dict)
d={1,2,3,4}#set，不可重复，无序，没有值的字典
d.add(5)#添加元素
del dict #全部删除，对象不在
del dict["a"]
dict.clear()#清空元素，对象还在

print(len(dict))
print(dict.keys())
print(dict.items())

for i in dict.keys():
    print(i,dict[i])
    pass
for i,v in dict.items():
    print(i,v)

#####函数的定义######
'''
函数由四份组成：
函数名称
函数体
参数列表
返回值

python中没有重载这一概念
python中如果想要在方法中修改全局变量，必须加上global，因为局部变量的作用范围只在方法内
并且不能再global前定义和全局变量同名的局部变量

'''
def fun(a,b):
    print("fun")
#不定长参数
def fun(a,b,*args,**kwargs):
    print(a)
    print(b)
    print("*args=",args)
    print("*kwargs=",kwargs)
#kwargs需要传key=value形式的
fun(1,2,3,4,5,6,7,x=1,y=2)
def fun1(a,b):
    return a+b,a-b,a*b,a/b;#返回一个元组

count = 100
def fun2():
    global count
    print(count)
    count =20
    print(count)
    pass
print(count)
fun2()
print(count)

########斐波那契数列############
def getNum(a):
    if(a<=2):
        return 1
    else:
        return getNum(a-1)+getNum(a-2)
############匿名函数#################
sum = lambda a,b:a+b
print(sum(1,2))
#用法1 参数
def opt(a,b,opt):
    print(a)
    print(b)
    print(opt(a,b))
    pass
fun(1,2,lambda a,b:a+b)
#用法2 排序作为内置函数使用
dict = [{"name":"张三","age":200},{"name":"张三","age":300}]
dict.sort(key=lambda x:x["age"])


