class Person(object):
    def __init__(self,name):
        self.name = name
        pass
    def work(self,type):
        print(self.name+"开始工作")
        axe = Factory.getAxe(type)
        axe.cutTree()

class Factory(object):
    @staticmethod
    def getAxe(type):
        if type == "stone":
            return Stone()
        elif type == "stell":
            return Steel()
        else:
            print("参数错误")

class Axe(object):
    def __init__(self,name):
        self.name = name
        pass
    def cutTree(self):
        print("使用"+self.name+"砍树")

class Stone(Axe):
    def __init__(self):
        pass
    def cutTree(self):
        print("使用石头砍树")
class Steel(Axe):
    def __init__(self):
        pass
    def cutTree(self):
        print("使用钢砍树")


p = Person("张三")
p.work("stell")