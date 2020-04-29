from pymongo import MongoClient
#实例化client
client = MongoClient(host = "127.0.0.1",port = 27017)
collection  = client["test"]["t251"]

# #插入一条数据
# coll = collection.insert({"name":"xiaowang","age":10});
# print(coll)
# #插入多条数据
# data_list = [{"name":"test{}".format(i)} for i in range(10)]
# collection.insert_many(data_list)
# t = collection.find({"name":"xiaowang"})
# collection.update({"":""})

#批量插入数据
data_list = [{"_id":i,"name":"py{}".format(i)} for i in range(1000)]
collection.insert_many(data_list)

#查询数据
ret = collection.find()
data_list = list(ret)
data_list = [i for i in data_list if["_id"]%100 == 0 and i["_id"] !=0]
print(data_list)
