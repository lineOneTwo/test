# coding:utf-8
__author__ = 'xiaoying'
'''
description:driver配置
'''
from appium import webdriver

# 使用正则表达式筛选设备 id
import re

# 使用time.sleep(xx)函数进行等待
import time

# 使用 os 模块调用命令
import os


def get_driver():
    # try:
    #     desired_caps = {
    #         'appPackage': 'com.icourt.alpha',
    #         'appActivity': '.module.other.WelcomeActivity',#被测程序启动时的Activity
    #         'platformName': 'Android',
    #         # 'unicodeKeyboard': 'true' , # 是否支持unicode的键盘。如果需要输入中文，要设置为“true”
    #         # 'resetKeyboard': 'true',  # 是否在测试结束后将键盘重轩为系统默认的输入法。
    #         # 'newCommandTimeout': '120',  # Appium服务器待appium客户端发送新消息的时间。默认为60秒
    #         # 'platformVersion': '6.0.1',
    #         # 'deviceName': 'OPPO A57',
    #         # 'udid': 'fb57ca3a',
    #         'noReset': True, # true:不重新安装APP，false:重新安装app
    #         'automationName': 'uiautomator2',
    #
    #     }
    #     self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
    # -*- coding: utf-8 -*-

    # 测试的包的路径和包名
    appLocation = " /Users/Downloads/app.apk "

    # 读取设备 id
    readDeviceId = list(os.popen('adb devices').readlines())

    # 正则表达式匹配出 id 信息
    deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]

    # 读取设备名
    deviceName = os.popen('adb shell getprop ro.product.model').read()

    # 读取设备系统版本号
    deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
    deviceVersion = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]

    # 读取 APK 的 package 信息
    # appPackageAdb = list(os.popen('aapt dump badging ' + appLocation).readlines())
    # appPackage = re.findall(r'\'com\w*.*?\'', appPackageAdb[0])[0]

    # # 删除以前的安装包
    # os.system('adb uninstall ' + appPackage)
    # print(deviceName)

    desired_caps = {
        'appPackage': 'com.icourt.alpha',
        'platformName': 'Android',
        'platformVersion': deviceVersion,
        'deviceName': deviceName,
        # 'appPackage': appPackage,
        # 'appWaitPackage': appPackage,
        # 'app': appLocation,
        # 'appActivity': appPackage + ".PageSplash",
        'appActivity': '.module.other.WelcomeActivity',
        'noReset': True,
        'udid': deviceId,
        'recreateChromeDriverSessions': True,
        'newCommandTimeout':120,
        'chromeOptions':{'androidProcess': 'com.icourt.alpha'},
        # 处理无法输入中文的问题
        'unicodeKeyboard': True,  # 使用unicodeKeyboard的编码方式来发送字符串
        'resetKeyboard': True,  # 将键盘给隐藏起来
        "recreateChromeDriverSessions": True,
        "chromedriverChromeMappingFile": "/usr/local/lib/node_modules/appium/node_modules/appium-chromedriver/chromedriver/chromeDriverMapping.json",
        "chromedriverExecutableDir": "/usr/local/lib/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac"
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    return driver
