import unittest

class Test04(unittest.TestCase):

    def setUp(self):
        print("Test04 --> setUp被执行了")
    def tearDown(self):
        print("Test04 --> tearDown被执行了")
    def test04(self):
        print("test04被执行了")