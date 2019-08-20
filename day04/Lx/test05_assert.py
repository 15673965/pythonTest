import unittest

class Test05(unittest.TestCase):

    def test001(self):
        # self.assertEqual(1,1)
        self.assertIn("admin", "你好，adm1in")
