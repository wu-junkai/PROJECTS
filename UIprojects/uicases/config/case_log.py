#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@version: python3.7
@author: wjk
@software: PyCharm
@file: case_log.py
@time: 2020/10/31 23:51
@description: None
"""
import allure


class ClassLog(object):
    feature = allure.feature  # 标注主要功能模块
    step = allure.step  # 标注测试用例的重要步骤
    stroy = allure.story  # 标注测试用例的场景
    severity = allure.severity  # 标注测试用例的重要级别
    description = allure.description  # 标注测试用例的描述

