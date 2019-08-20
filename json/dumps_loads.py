import json

data = {
    'name': 'Connor',
    'sex': 'boy',
    'age': 26
}
print(data)
# json.dumps()用于将字典形式的数据转化为字符串，json.loads()用于将字符串形式的数据转化为字典
data1 = json.dumps(data)
print(data1)
data2 = json.loads(data1)
print(data2)
print(type(data))  # 输出原始数据格式
print(type(data1))  # 输出经过json.dumps的数据格式
print(type(data2))  # 输出经过json.loads的数据格式

# 如果直接将dict类型的数据写入json文件中会发生报错，因此在将数据写入时需要用到json.dump(),


# json.load()用于从json文件中读取数据.

with open('data3.json', 'a', encoding='utf-8') as f:
    f.write(data1)
    f.close()
data4 = json.load(open('data3.json'))  # json.load（）用于读取json数据
print(type(data4))
print(data4)
