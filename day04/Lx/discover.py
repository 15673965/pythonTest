import unittest

if __name__ == '__main__':
    # 使用unittest.defaultTestLoader()类，通过该类下面的discover()方法自动搜索指定目录下指定开头
    # 的.py文件，并将查找到的测试用例组装到测试套件；
    '''定义测试套件'''
    discover = unittest.defaultTestLoader.discover("../Case/", pattern="test*.py")
    # 运行测试套件
    unittest.TextTestRunner().run(discover)