# 导入suite
import unittest
# 导入用例
from day04.Case.test01 import Test01
from day04.Case.test02 import Test02
from day04.Case.test03 import Test03

if __name__ == '__main__':
    # 实例化suite
    suite = unittest.TestSuite()

    # 添加用例方法
    suite.addTest(Test01("test01"))
    suite.addTest(Test02("test02"))
    suite.addTest(Test03("test03"))

    # 实例化TestRunner
    runner = unittest.TextTestRunner()

    # 执行用例
    runner.run(suite)