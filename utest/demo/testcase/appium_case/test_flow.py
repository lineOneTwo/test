#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import unittest

from common.appium_common.element_action import *
from common.appium_common.session import *
from utx import *


class TestAboutSend(unittest.TestCase):
    """
    用户登录
    跳过权限弹窗
    找到联系人发送消息
    """

    @classmethod
    def setUpClass(cls):  # setUpClass所有用例开始前执行一遍，但是必须使用类函数装饰器
        cls.user_number = 18636299591
        cls.password = 123456
        cls.app = '牛老幺'
        cls.driver = driver_begin(cls.app)

        log.debug("初始化APP，测试数据初始化")

    @tag(Tag.UI_F1)
    def test_login(self):
        """测试登陆操作"""
        time.sleep(1)
        log.info("开始执行登录操作")
        log.info("----" * 15)
        inputting(driver=self.driver, elements_name=2, section_name='登录页面', name='输入框', txt=self.user_number)
        log.info("输入账号")
        inputting(driver=self.driver, elements_name=2, section_name='登录页面', name='密码', txt=self.password)
        log.info("输入密码")
        clicking(driver=self.driver, elements_name=2, section_name='登录页面', name='登录按钮')
        log.info("点击登录")

    @tag(Tag.UI_F1)
    def test_skip_limits(self):
        """第一次进入APP的权限弹窗"""
        time.sleep(2)
        log.info("操作权限弹窗三次")
        for i in range(3):
            clicking(driver=self.driver, elements_name=2, section_name='权限', name='允许')
            time.sleep(1.5)

    @skip("调试阶段无序执行")
    def test_create_user_name(self):
        """修改昵称"""
        log.info("进入我的")
        clicking(driver=self.driver, elements_name=2, section_name='导航', name='我的')
        log.info("进入我的个人信息")
        clicking(driver=self.driver, elements_name=2, section_name='我的', name='个人信息')
        log.info("点击昵称进行修改")
        clicking(driver=self.driver, elements_name=2, section_name='我的', name='昵称')
        log.info("返回")
        clicking(driver=self.driver, elements_name=2, section_name='我的', name='返回')
        clicking(driver=self.driver, elements_name=2, section_name='我的', name='返回')

    @tag(Tag.UI_F1)
    def test_send_massage(self):
        """发送消息给好友"""
        log.debug("进入通讯录")
        clicking(driver=self.driver, elements_name=2, section_name='导航', name='通讯录')
        log.debug("找到李飞")
        clicking(driver=self.driver, elements_name=4, section_name='通讯录', name='李飞')
        log.info("准备发送100条消息")
        clicking(driver=self.driver, elements_name=2, section_name='好友', name='发送消息')
        for i in range(100):
            inputting(driver=self.driver, elements_name=2, section_name='好友', name='消息输入框', txt='你好')
            clicking(driver=self.driver, elements_name=2, section_name='好友', name='发送按钮')
            log.info("发送第" + str(i + 1) + "成功，发送消息内容“你好”")
    def test_111(self):
        print("ssssssssssssssssssssssssssssssss"*100)
