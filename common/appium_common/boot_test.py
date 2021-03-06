# -*- coding: utf-8 -*-
import os
import re
import subprocess
import time

# 执行shell
def shell(cmd):
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    (stdout_output, err_output) = p.communicate()
    if err_output != None and len(err_output) != 0:
        print("Shell err_output: " + str(err_output))
    # print("stdout_output: " + str(stdout_output))
    return stdout_output


# 启动app应用
def app_start(package_name, launch_activity, device_id=''):
    if device_id != '':
        cmd_start = "adb -s %s shell am start -n %s" % (device_id, package_name + "/" + launch_activity)
    else:
        cmd_start = "adb shell am start -n %s" % (package_name + "/" + launch_activity)
    shell(cmd_start)
    time.sleep(3)
    # print("App start success: " + str(cmd_start))


# 退出app应用
def app_stop(package_name, device_id=''):
    if device_id != '':
        cmd_stop = "adb -s %s shell am force-stop %s" % (device_id, package_name)
    else:
        cmd_stop = "adb shell am force-stop %s" % (package_name)
    shell(cmd_stop)
    time.sleep(1)
    # print("App stop finishes: " + str(cmd_stop))


# 判断app应用是否在前台
def is_activity_started(package_name, device_id=''):
    if device_id != '':
        cmd_current_activity = 'adb -s %s shell dumpsys activity activities | sed -En -e "/Running activities/,/Run #0/p"' % device_id
    else:
        cmd_current_activity = 'adb shell dumpsys activity activities | sed -En -e "/Running activities/,/Run #0/p"'
    print(cmd_current_activity)
    cmd_result = str(shell(cmd_current_activity))
    # 如果当前应用处于前台或resume后台状态，返回True
    if package_name in cmd_result:
        return True
    else:
        return False


# 设置app应用后台运行
def set_activity_backup(package_name, launch_activity, device_id=''):
    if device_id != '':
        # if not is_activity_started(package_name, device_id):
        app_start(package_name, launch_activity, device_id)
        cmd = 'adb -s %s shell input keyevent key 3' % device_id
    else:
        # if not is_activity_started(package_name):
        app_start(package_name, launch_activity)
        cmd = 'adb shell input keyevent key 3'
    shell(cmd)

# 获取冷启动时间
def get_cold_boot_time(package_name, launch_activity, device_id=''):
    # if is_activity_started(package_name, device_id):
    app_stop(package_name, device_id)
    if device_id != '':
        cmd_start = "adb -s %s shell am start -W %s | findstr WaitTime" % (
            device_id, package_name + "/" + launch_activity)
    else:
        cmd_start = "adb shell am start -W %s | findstr WaitTime" % (package_name + "/" + launch_activity)
    cold_boot_time = shell(cmd_start)[10:].strip()
    print('冷启动时间' + str(cold_boot_time))

    return int(cold_boot_time)

# 获取热启动时间
def get_hot_boot_time(package_name, launch_activity, device_id=''):
    set_activity_backup(package_name, launch_activity, device_id)
    if device_id != '':
        cmd_start = "adb -s %s shell am start -W %s | findstr WaitTime" % (
            device_id, package_name + "/" + launch_activity)
    else:
        cmd_start = "adb shell am start -W %s | findstr WaitTime" % (package_name + "/" + launch_activity)
    cold_boot_time = shell(cmd_start)[10:].strip()
    print('热启动时间' + str(cold_boot_time))
    return int(cold_boot_time)


# 执行测试，times为次数，结果取平均值
def run_test(times):
    cold_time = []
    hot_time = []
    # 读取设备 id
    read_device_id = list(os.popen('adb devices').readlines())

    # 正则表达式匹配出 id 信息
    device_id = re.findall(r'^\w*\b', read_device_id[1])[0]

    for i in range(times):
        cold_time.append(get_cold_boot_time('com.foryou.agent', '.appentry.EntryActivity'))
        hot_time.append(get_hot_boot_time('com.foryou.agent', '.appentry.EntryActivity', device_id))
    res_cold_time = 0
    res_hot_time = 0
    print("冷启动时间 = " + str(cold_time))
    print("热启动时间 = " + str(hot_time))
    for i in cold_time:
        res_cold_time = res_cold_time + i
    print('平均冷启动时间: ' + str(res_cold_time / times) + ' ms')
    for i in hot_time:
        res_hot_time = res_hot_time + i
    print('平均热启动时间: ' + str(res_hot_time / times) + ' ms')
# 执行次
run_test(5)
