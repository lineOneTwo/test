from appium import webdriver

from common.appium_common.read_config import read_ini
from config.appium_conf.load_file import load_file


def driver_begin(app):
    package_name = read_ini(ini_file_path=load_file(5), name=app, value='appPackage')
    activity_name = read_ini(ini_file_path=load_file(5), name=app, value='appActivity')
    print(package_name, activity_name)
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'OPPOr11s',
        'platformVersion': '9',
        'appPackage': package_name,
        'appActivity': activity_name,
        'noReset': False,
        'resetKeyboard': False  # 将键盘给隐藏起来
        # 'unicodeKeyboard': True,# 使用unicodeKeyboard的编码方式来发送字符串
    }
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
