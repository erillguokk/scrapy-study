class Single(object):
    __instance = None
    __First_init = True
    def __init__(self,name):
        if self.__First_init:
            self.__First_init = False
            self.name = name
            print("init")
    def __new__(cls,name):
        if not cls.__instance:#判断是否为空，为空往下执行
            print("new")
            cls.__instance = object.__new__(cls)
            pass
        return cls.__instance;
s = Single("张三")
print(s.name)
s1 = Single("李四")
print(s1.name)
print(s == s1)