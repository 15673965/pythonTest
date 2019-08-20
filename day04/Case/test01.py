import unittest

class Test01(unittest.TestCase):

    def setUp(self):
        print("Test01 --> setUp被执行了")
    def tearDown(self):
        print("Test01 --> tearDown被执行了")
    def test01(self):
        print("test01被执行了")