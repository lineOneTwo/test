import hashlib
import datetime
import unittest
import pymysql
import time
import inspect
import linecache
import requests
import json
import random
import re
import socket
import sys
import xlrd
from xlutils.copy import copy
from datetime import datetime, timedelta
from sshtunnel import SSHTunnelForwarder
from retry import retry
import xlwt
import xpinyin

from common.api_common.conf import *


@retry(Exception, tries=3, delay=2)
def remote_database(database, sql):
    # 获取数据库配置信息
    env = get_config('default', 'environment')
    db_port = 3306
    if env == '':
        server_host = get_config('database_online', 'server_host')
        server_port = get_config('database_online', 'server_port')
        server_user = get_config('database_online', 'server_user')
        server_password = get_config('database_online', 'server_password')
        db_host = get_config('database_online', 'db_host')
        db_user = get_config('database_online', 'db_user')
        db_password = get_config('database_online', 'db_password')
    elif env[0] == 't' or env[0] == 'r' or env[0] == 'd':
        server_host = get_config('database_test', 'server_host')
        server_port = get_config('database_test', 'server_port')
        server_user = get_config('database_test', 'server_user')
        server_password = get_config('database_test', 'server_password')
        db_host = get_config('database_test', 'db_host')
        db_port = get_config('database_test', 'db_port_%s' % env)
        db_user = get_config('database_test', 'db_user')
        db_password = get_config('database_test', 'db_password')
    elif env[0] == 'd':
        db_host = get_config('database_develop', 'host')
        db_port = get_config('database_develop', 'port')
        db_user = get_config('database_develop', 'user')
        db_password = get_config('database_develop', 'password')
    else:
        pass
    sql_function = str.lower(sql[:3])
    hostname = socket.getfqdn(socket.gethostname())
    try:
        myaddr = socket.gethostbyname(hostname)
    except:
        myaddr = socket.gethostbyname("")
    if myaddr != "192.168.2.68":
        if env in ('s1', 's2'):  # 无需跳板机
            db = pymysql.connect(host=db_host, port=int(db_port), user=db_user, password=db_password, db=database,
                                 charset='utf8')
            cursor = db.cursor()
            cursor.execute(sql)
            if sql_function == 'sel':
                data = cursor.fetchall()
                cursor.close()
                db.close()
                data_1 = []
                for i in data:
                    j = list(i)
                    data_1.append(j)
                return data_1
            else:
                db.commit()
            db.close()
        else:
            with SSHTunnelForwarder((server_host, int(server_port)), ssh_password=server_password,
                                    ssh_username=server_user,
                                    remote_bind_address=(db_host, int(db_port)), ) as server:
                db = pymysql.connect(host='127.0.0.1', port=server.local_bind_port, user=db_user,
                                     password=db_password,
                                     db=database, charset='utf8')
                cursor = db.cursor()
                cursor.execute(sql)
                if sql_function == 'sel':
                    data = cursor.fetchall()
                    cursor.close()
                    db.close()
                    data_1 = []
                    for i in data:
                        j = list(i)
                        data_1.append(j)
                    return data_1
                else:
                    db.commit()
                db.close()
    else:
        try:
            db = pymysql.connect(host='192.168.1.29', port=int(db_port), user='fykctest', password='fykctest_88',
                                 db=database, charset='utf8')
            cursor = db.cursor()
            cursor.execute(sql)
            if sql_function == 'sel':
                data = cursor.fetchall()
                cursor.close()
                db.close()
                data_1 = []
                for i in data:
                    j = list(i)
                    data_1.append(j)
                return data_1
            else:
                db.commit()
            db.close()
        except:
            return "连接数据库失败"


# 执行数据库文件
def remote_sql_file(database, sql_file_name):
    with open(sql_file_name, 'r+', encoding='utf-8') as f:
        sql_list = f.read().split(';')[:-1]  # sql文件最后一行加上;
        sql_list = [x.replace('\n', '') if '\n' in x else x for x in sql_list]  # 将每段sql里的换行符改成空格
        # 执行sql语句，使用循环执行sql语句
        print(sql_list)
        for sql_item in sql_list:
            print(sql_item)
            remote_database(database, sql_item)  # 执行sql


# 生成URL
def mk_url(client, url_path='', third_sign='', external=False):
    try:
        env = os.environ['APP_ENV']
    except:
        env = get_config('default', 'environment')
    suffix = {
        'approval': ['approval', 'fykc-approval-service'],  # 审批系统
        'bms': ['bms', 'fykc-bms-wrapper'],  # 运单系统
        'caiwu': ['caiwu', 'fykc-caiwu-service'],  # 财务系统
        'dd': ['dd', 'fykc-truck-scheduler'],  # 调度系统
        'erobot': ['fuwu', 'fykc-erobot.wrapper-service'],  # erobot
        'fuwu': ['fuwu', 'fykc-house-keeper'],  # 服务系统
        'im': ['fuwu', 'fykc-imadmin-wrapper'],  # IM
        'jr': ['jr', 'fykc-financeana-service'],  # 金融系统
        'ny': ['ny', 'fykc-oilassign-service'],  # 能源系统
        'oms': ['oms', 'fykc-oms-service'],  # 运营系统
        'order': ['order', 'fykc-order-core'],  # 运单
        'openapi': ['openapi', 'fykc-thirdwrapper-service'],  # 开放平台接口
        'pz': ['pz', 'fykc-conf-wrapper'],  # 配置系统
        'superbrain': ['superbrain', 'fykc-biddecision-service'],  # 招投标系统
        'taxsys': ['taxsys', 'fykc-taxsys-service'],  # 税务系统
        'truckfy': ['truckfy', 'fykc-truckforyou-service'],  # 专车系统
        'turing': ['turing', 'fykc-turing-service'],  # 图灵系统
        'user': ['user', 'fykc-crm-wrapper'],  # 用户系统
        'youka': ['youka', 'fykc-oilcard'],  # 油卡系统
        'yxd': ['yxd', 'fykc-autoquery-service'],  # 意向单系统
        'task': ['task', 'fykc-taskcenter-service'],  # 工作台系统
    }
    if external is True:
        url = 'https://%sproxy.fuyoukache.com/%s' % (env, url_path)
    elif client in suffix.keys() and third_sign == '':
        url = 'https://%s%s.fuyoukache.com/service/%s/%s' % (env, suffix[client][0], suffix[client][1], url_path)
    elif client == 'nopen' and third_sign != '':
        url = 'https://%snopen.fuyoukache.com/%s?appKey=%s&reqTimestamp=%s&signStr=%s' % (
            env, url_path, third_sign['app_key'], third_sign['time_stamp'], third_sign['sign_str'])
    elif client == 'admin.niudun':
        url = 'http://%sadmin.niudun.fuyoukache.com/%s' % (env, url_path)
    else:
        url = 'https://%s%s.fuyoukache.com/%s' % (env, client, url_path)
    print(url)
    return url


# md5加密
def md5_encrypt(text):
    m = hashlib.md5()
    text_1 = text.encode()
    m.update(text_1)
    md5value = m.hexdigest()
    return md5value


# 获取京东sign
def sign():
    a = '%s&%s&%s' % (get_config('open', 'app_key_jd'), int(time.time()), get_config('open', 'app_secret_jd'))
    third_sign = {
        "app_key": get_config('open', 'app_key_jd'),
        "time_stamp": int(time.time()),
        "sign_str": md5_encrypt(a)
    }
    return third_sign


# 获取跨越sign
def ky_sign():
    a = '%s&%s&%s' % (get_config('open', 'app_key_ky'), int(time.time()), get_config('open', 'app_secret_ky'))
    third_sign = {
        "app_key": get_config('open', 'app_key_ky'),
        "time_stamp": int(time.time()),
        "sign_str": md5_encrypt(a)
    }
    return third_sign


def get_function_name():
    """获取正在运行函数(或方法)名称"""
    return inspect.stack()[1][3]


def get_all_in_path(path):
    """获取路径下的各类型文件"""
    path_dic = {}
    for root, dirs, files in os.walk(path):
        file_dic = {
            'dirs': dirs,
            'files': files
        }
        path_dic[root.replace('/', '\\').split('\\')[-1]] = file_dic
    return path_dic


def get_file_list_by_time(file_path):
    dir_list = os.listdir(file_path)
    if not dir_list:
        return
    else:
        # 注意，这里使用lambda表达式，将文件按照最后修改时间顺序升序排列
        # os.path.getmtime() 函数是获取文件最后修改时间
        # os.path.getctime() 函数是获取文件最后创建时间
        dir_list = sorted(dir_list, key=lambda x: os.path.getmtime(os.path.join(file_path, x)))
        # print(dir_list)
        return dir_list


def base_request(client, url_path, method='post', file_path='', data={}, cookies='', expected={}, actual={},
                 assert_flag=True):
    """请求的封装"""
    url = mk_url(client, url_path)
    print('请求url：' + url)
    print('请求cookies：' + str(cookies))
    print('请求参数data：' + str(data))

    if file_path == '':
        r = eval('requests.' + method + '(url, data=data,cookies=cookies)')
    else:
        with open(file_path, "rb") as f:
            r = eval(
                'requests.' + method + '(url,data=data,files={"file":f},cookies=cookies)')
    print('返回结果' + r.text)
    assert r.status_code == 200
    if assert_flag is True:
        try:
            r_json = r.json()
        except:
            print('r.json()不存在')
        else:
            if expected != {} and actual != {}:
                unittest.TestCase().assertEqual(expected, actual)
            elif 'status' in dict(r_json).keys():
                unittest.TestCase().assertIn(r_json['status']['code'], [0, 2, 3, 250])
                unittest.TestCase().assertIn(r_json['status']['desc'],
                                             ['操作成功', '您的操作过于频繁,请稍后再试！', '结果为空', '余额不足，请先充值！'])

    return r


def get_strf_time(days=0, weeks=0, hours=0, minutes=0, seconds=0, milliseconds=0, microseconds=0,
                  strf='%Y-%m-%d %H:%M:%S'):
    """
    格式化时间
    :param days:
    :param weeks:
    :param hours:
    :param minutes:
    :param seconds:
    :param milliseconds:
    :param microseconds:
    :param strf:
    :return:
    """

    strf_time = (datetime.now() + timedelta(days=days, seconds=seconds, microseconds=microseconds,
                                            milliseconds=milliseconds,
                                            minutes=minutes, hours=hours, weeks=weeks)).strftime(strf)
    return str(strf_time)


def read_excel(excel_name, row, col, sheet_index=0):
    """
    读取excel
    :param excel_name: 文件名称
    :param sheet_index: sheet
    :param row: 行
    :param col: 列
    :return: 某行某列的值
    """
    try:
        excel = xlrd.open_workbook(excel_name)  # 读取指定的Excel
        table = excel.sheet_by_index(sheet_index)  # 获取Excel的第一个sheet
        print(table.cell(row, col).value)
        return table.cell(row, col).value
    except Exception:
        print("打开execl文件出错")


def write_excel(excel_path, row, col, write_value, sheet_index=0):
    """
    excel写入(只能写入xls文件,不能写入xlsx文件。)
    :param excel_path: excel路径
    :param sheet_index: sheet
    :param row: 行
    :param col: 列
    :param write_value: 写入的值
    :return:
    """
    style1 = xlwt.XFStyle()
    rb = xlrd.open_workbook(excel_path, formatting_info=True)
    # 复制
    new_excel = copy(rb)
    # 取sheet表
    excel_sheet = new_excel.get_sheet(sheet_index)
    excel_sheet.write(row, col, write_value, style1)
    new_excel.save(excel_path)


def mobile_create():
    """手机号生成"""
    time.sleep(0.01)
    mobile = int('10' + str(time.time() * 1000).replace('.', '')[4:13])
    return mobile


def time_stamp_create(days=0, times='20:48:57'):
    """生成指定时间时间戳，默认第二天12点"""
    if days >= 0:
        time_string = str(datetime.today().date() + timedelta(days=int(days))) + ' ' + times
    else:
        time_string = str(datetime.today().date() - timedelta(days=abs(int(days)))) + ' ' + times
    print('生成时间：', time_string)
    time_array = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
    time_stamp = int(time.mktime(time_array) * 1000)
    return time_stamp


def time_stamp_to_date(time_stamp):
    # 转换成localtime
    time_local = time.localtime(time_stamp)
    # 转换成新的时间格式(2016-05-05 20:28:54)
    time_date = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return time_date


# 生成指定位数的随机数
def random_number(num):
    list_number = []
    for number in range(num):
        str_number = str(random.randint(0, 9))
        list_number.append(str_number)
    numbers = " ".join(list_number).replace(" ", "")
    return numbers


# 发送消息到企业微信
def send_msg_to_wx(msg, wx_url=list(), groups=None, users=None):
    # print(wx_url)
    headers = {
        "Content-Type": "application/json; charset=UTF-8"
    }
    wx_urls = list()
    if len(wx_url) != 0:
        for temp_wx_url in wx_url:
            if temp_wx_url != '':
                wx_urls.append(temp_wx_url)
    # 通知自动化通知群
    wx_urls.append('https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=da4273ef-9e0d-4971-a9ed-1938cd932123')
    send_mobile_list = ''
    if users is not None:
        user = xpinyin.Pinyin().get_pinyin(users)
        user = user.replace('-', '')
        if user in user_info.keys():
            send_mobile_list += user_info[user]['mobile']
            send_mobile_list += ','
    if groups is not None:
        for group in groups.replace(' ', '').split(','):
            group_users = tag_contact[group]['users']
            group_robot_address = tag_contact[group]['wx_robot_address']
            if group_users == 'all':
                send_mobile_list += '@all'
                send_mobile_list += ','
            else:
                for user in group_users.replace(' ', '').split(','):
                    send_mobile_list += user_info[user]['mobile']
                    send_mobile_list += ','
            if group_robot_address != '':
                wx_urls.append(group_robot_address)

    send_mobile_list = list(set(send_mobile_list.replace(' ', '').split(',')))
    # print(send_mobile_list)
    array = {
        "msgtype": "text",
        "text": {
            "content": msg,
            "mentioned_mobile_list": send_mobile_list,
        }
    }
    print('消息通知: ', wx_urls)
    for wx_url in wx_urls:
        res = requests.post(wx_url, json=array, headers=headers)
    # return res



