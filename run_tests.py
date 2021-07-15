import sys
import time

sys.path.append('./interface')
sys.path.append('./db_fixture')
from HTMLTestRunner import HTMLTestRunner
import unittest
from db_fixture import test_data

# 指定测试用例为当前文件夹下的 interface 目录
test_dir = r'D:\Program Files\JetBrains\PyCharm Community Edition 2020.2\test\interface'
# 执行指定格式的用例
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

if __name__ == "__main__":
    # 初始化接口测试数据
    test_data.init_data()
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # filename = r'D:\Program Files\JetBrains\PyCharm Community Edition 2020.2\test\report\\\\' + now + '_result.html'
    filename = r'..\test\report\\\\' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Interface Test Report',
                            verbosity=1,
                            description='Implementation Example with: ')
    runner.run(discover)
    fp.close()
