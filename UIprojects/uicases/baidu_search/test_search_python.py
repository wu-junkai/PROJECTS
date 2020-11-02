#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@version: python3.7
@author: wjk
@software: PyCharm
@file: test_search_python.py
@time: 2020/10/31 23:26
@description: None
"""

import allure
from selenium import webdriver
from time import sleep
from uictrl.urls.urls import Urls
from ..config.case_log import ClassLog
from uictrl.public_method.exceptions import ResultException


class TestCase(object):
    @allure.title('百度：UI自动化测试')
    @allure.feature('测试百度首页输入框')
    def setup_class(self):
        print(u'打开浏览器')
        self.browser = webdriver.Chrome()
        self.browser.get(Urls.baidu_url)
        self.browser.implicitly_wait(5)
        self.browser.maximize_window()

    @allure.story(u'百度输入框清空验证')
    def test_open_baidu_search_bag(self):
        with ClassLog.step(u'百度输入框输入bag并清空'):
            self.browser.find_element_by_css_selector('.s_ipt').send_keys(u'bag')
            sleep(1)
            input_text = self.browser.find_element_by_css_selector('.s_ipt')
            try:
                input_text.clear()
            except Exception as e:
                raise ResultException(u'清除失败，错误信息：%s' % e)
            sleep(1)
            self.browser.find_element_by_css_selector('.s_btn').click()
            sleep(1)
            assert True

    @allure.story('百度输入框输入验证')
    def test_open_baidu_search_python(self):
        with ClassLog.step('百度输入框输入python'):
            self.browser.find_element_by_css_selector('.s_ipt').send_keys(u'python')
            self.browser.find_element_by_css_selector('.s_btn').click()
            sleep(1)
            assert True

    def teardown_class(self):
        self.browser.close()
