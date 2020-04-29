#######类########
'''
init在完成对象初始化，在对象创建完成之后，立即被调用执行，隐式调用，参数必须跟创建对象传递的参数保持一致
new构造方法，创建对象的时候，首先调用的是这个方法，方法必须要有返回值，参数必须跟创建对象传递的参数保持一致
无论什么情况，init和new方法的参数都要保持一致
'''
class Person(object):
    def __init__(self,name,age,salary):#并非是构造器，只是初始化的作用,每次调用new都会隐式调用这个方法
        self.name = name
        self.age = age
        self.__salary = salary #定义私有属性,两个下划线
        pass
    def __new__(cls, name, age, salary):  # 构造器
        return object.__new__(cls)  # 调用父类的构造器
    def __str__(self):#类似于tostring
        return "hahah"
    def __del__(self):#在整个python文件执行完毕只有销毁
        print("--del---")
    def getSalary(self):
        return self.__salary
    def setSalary(self,salary):
        self.__salary = salary
    def eat(self):#self类似于java中的this
        self.__test()#调用私有方法
        pass#占位符
    def __test(self):#定义私有方法
        print(self.__salary)

p = Person("张三",12,300)
print(p.name)
p.eat()
print(p)
print(p.getSalary())
print(id(p))#获取这个对象的内存地址
del p #是删除这个p的引用，内存空间并没有回收

'''
python支持多继承
'''
class Animal(object):
    def __init__(self,name):
        self.name = name
        pass
    def run(self):
        print(self.name)
class Cat(Animal):
    def __init__(self,name,type):
        super().__init__(name)
        self.name = name
        self.type = type

cat = Cat("miaomiao","cat")
cat.run()

class A(object):
    def show(self):
        print("show   a")
        pass
    pass
class B(object):
    def show(self):
        print("show   b")
        pass
    pass
class C(A,B):
    pass
c = C();
c.show()

'''
python的多态，崇尚鸭子模型，因为没有类型指定，并不能算作严格意义上的多态
'''
class F1(object):
    def show(self):
        print("myshow")
def Fun(obj):
    obj.show()

f =F1();
Fun(f)

''''类属性和实例属性的区别'''
class Person(object):
    name = "zhangsan"
    __age = 200
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def getAge(self):
            return self.__age
    @classmethod#类方法，访问的是类的属性
    def getAge2(cls):
        return cls.__age
    @staticmethod#同样访问的是类属性，不会随着init赋值而改变
    def getAge3():
        return Person.__age

print(Person.name)
Person.name = "王五"
p = Person("lisi",300)
print(p.name)
print(p.getAge())
print(p.getAge2())
print(Person.name)
