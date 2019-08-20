import json

class Student(object):
    def __init__(self, name, age, score):
        self.__name = name
        self.__age = age
        self.__score = score

    def student2dict(self):
        return {
            'name': self.__name,
            'age': self.__age,
            'score': self.__score
        }
if __name__ == '__main__':
    data1 = dict(name='Bob', age=20, score=88)
    print(type(data1))
    print(data1)
    print("-"*20)

    # json字符串反序列化成dict对象
    json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    data2 = json.loads(json_str)
    print(type(data2))
    print(data2)
    print("-" * 20)

    # Class 对象序列化成json字符串
    s = Student('tonny', 20, 59)
    data3 = json.dumps(s, default=Student.student2dict)
    print(type(data3))
    print(data3)