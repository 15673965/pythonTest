import unittest

class Test03(unittest.TestCase):

    def setUp(self):
        print("Test03 --> setUp被执行了")
    def tearDown(self):
        print("Test03 --> tearDown被执行了")
    def test03(self):
        print("test03被执行了")