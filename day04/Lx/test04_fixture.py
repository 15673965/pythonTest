import unittest

class Test04(unittest.TestCase):

    # 初始化首先被执行
    def setUp(self):
        print("setUp被执行")

    # 结束方法最后执行
    def tearDown(self):
        print("tearDown被执行")

    def test001(self):
        print("test001被执行")

    def test002(self):
        print("test002被执行")

if __name__ == '__main__':

    # 自动搜索当前中以test开头的函数并执行
    unittest.main()