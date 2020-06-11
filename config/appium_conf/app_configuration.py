# —*- coding:utf-8 -*-
#Created by Administrator on 2020/6/11
#Copyright (C) 2020 $USER.All rights reserved.
# 读取 APK 的 package 信息
import os
import re  # 读取设备 id
appLocation=""
readDeviceId = list(os.popen('adb devices').readlines())

# 正则表达式匹配出 id 信息
deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]

# 读取设备名
deviceName = os.popen('adb shell getprop ro.product.model').read()

# 读取设备系统版本号
deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
deviceVersion = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]

#读取 APK 的 package 信息
appPackageAdb = list(os.popen('aapt dump badging ' + appLocation).readlines())
appPackage = re.findall(r'\'com\w*.*?\'', appPackageAdb[0])[0]

# 删除以前的安装包
os.system('adb uninstall ' + appPackage)
print(deviceName)
