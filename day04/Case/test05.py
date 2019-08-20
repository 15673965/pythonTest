import unittest

class Test05(unittest.TestCase):

    def setUp(self):
        print("Test05 --> setUp被执行了")
    def tearDown(self):
        print("Test05 --> tearDown被执行了")
    def test05(self):
        print("test05被执行了")