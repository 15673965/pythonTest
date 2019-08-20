import unittest

class Test08(unittest.TestCase):

    def setUp(self):
        print("Test08 --> setUp被执行了")
    def tearDown(self):
        print("Test08 --> tearDown被执行了")
    def test08(self):
        print("test08被执行了")