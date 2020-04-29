'''文件操作
r读取操作，文件不存在抛异常
w写操作，文件不存在创建，文件存在就覆盖
a写操作，文件不存在创建，文件内容存在就追加
rb以二进制方式打开文件，即序列化
wb
ab
r+读写操作，写与读不分先后，即随时都可进行读与写，写是追加
w+读写操作，文件不存在创建，存在覆盖，先写后读。保证文件有内容通过移动光标来读自己想要的部分。
a+读写操作，文件不存在创建，存在就追加，任意时刻读写，若刚用‘a+’打开一个文件，则不能立即读，因为此时光标已经是文件末尾，除非你把光标移动到初始位置或任意非末尾的位置。
文件的定位读写
'''
with open("C://software//readme.txt","a+",encoding = "utf-8") as file:
    file.seek(0)
    s = file.readline()
    print(s)
    file.write("abcd")
# f = open("C://software//python//test.txt","w")
# f.write("abcd")
# # f.close()
#
# f = open("C://software//python//test.txt","r")
# content = f.read()
# content1 =  f.readline()#只读一行，从上一次读取的指针位置开始读取
# content2 = f.readLines();
# for i in  content2:
#     print(i)
# f.close()
#
#
#
# f = open("C://software//python//test.txt","a+")
#
# content = f.readline()
# f.tell()#获取当前指针的位置
# print(f.tell())
# f.seek(5,0)#0,文件开头，1-当前位置，2-文件结尾（偏移量应该为负数），偏移位置为5,设置文件操作的指针位置
# print(f.readline())


