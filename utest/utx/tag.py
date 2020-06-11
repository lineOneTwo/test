#! /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
测试用例标签类
"""

from enum import Enum, unique


class NewTag:
    def __init__(self, desc=""):
        self.desc = desc


@unique
class Tag(Enum):
    SMOKE = NewTag("冒烟")  # 冒烟测试标记，可以重命名，不要删除
    ALL = NewTag("完整")  # 完整测试标记，可以重命名，不要删除

    # 以下开始为扩展标签，自行调整
    UI_F1 = NewTag("UI自动化流程1")
    UI_F2 = NewTag("UI自动化流程2")
    UI_F3 = NewTag("UI自动化流程2")
    UI_F4 = NewTag("UI自动化流程2")
    UI_F5 = NewTag("UI自动化流程2")
    UI_F6 = NewTag("UI自动化流程2")
    UI_F7 = NewTag("UI自动化流程2")
    UI_F8 = NewTag("UI自动化流程2")
    UI_F9 = NewTag("UI自动化流程2")

    API_V1_0_0 = NewTag("接口自动化V1.0.0版本")
    API_V2_0_0 = NewTag("接口自动化V1.0.0版本")


