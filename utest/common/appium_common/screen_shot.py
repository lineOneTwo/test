import time


# 截图
from lib2to3.pgen2 import driver


def getScreenShot():
    time = getTime()
    filename = '../jpg/ %s.png' % time
    driver.get_screenshot_as_file(filename)


# 获取时间戳
def getTime():
    tamp = int(time.time())
    return tamp