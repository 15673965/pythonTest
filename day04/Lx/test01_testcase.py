# 导入unittest
import unittest

class Test01(unittest.TestCase):
# 必须是test开头
    def test01(self):
        print("test001被执行")

    def test02(self):
        print("test002被执行")
'''
1.不能以汉子、数字开头
2.不能含特殊字符、空格
3.命名重复，关键字不要使用
'''

