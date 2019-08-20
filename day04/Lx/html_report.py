import unittest,time
# 导入HTMLTestRunner
from day04.Common.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    # 添加测试套件
    discover = unittest.defaultTestLoader.discover("../Case/", pattern="test*py")
    # 定义html报告的位置
    dir_path = "../Report/"
    # 定义系统时间
    nowtime = time.strftime("%Y_%m_%d %H_%M_%S")
    # 定义文件
    file_name = dir_path + nowtime + "Report.html"
    # 给指定的报告写入数据
    with open(file_name,"wb") as f:
        # 实例化HTMLTestRunner并执行run()
        HTMLTestRunner(stream=f, title="Web自动化测试", description="W10系统，火狐浏览器").run(discover)



