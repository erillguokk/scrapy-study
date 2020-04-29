import threading
from queue import Queue


class Run():
    def __init__(self):
        self.queue = Queue()
        self.flag = True

    def run(self):
        self.queue.put(1)
        self.queue.put(2)
        print("子线程1结束了")

    def over(self):
        # print(self.queue.get())
        # self.queue.task_done()
        while self.flag :
            if self.queue.qsize()>0:
                print(self.queue.get())
                self.queue.task_done()
        print("子线程2结束了",end="\n\r")




if __name__ == '__main__':
    run = Run()
    threading.Thread(target= run.run).start()
    threading.Thread(target=run.over).start()
    run.queue.join()
    run.flag = False
    print("主线程结束了")
'''
经过测试，join必须和get和task_done一起配合，并且queue中有多少个元素，就需要get和task_done多少次
'''