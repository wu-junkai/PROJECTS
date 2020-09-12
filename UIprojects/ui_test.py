# coding=utf-8
import pytest
from selenium import webdriver
from time import sleep


class TestCase:

    def setup_class(self):
        print(u'打开浏览器')
        self.browser = webdriver.Chrome()
        self.browser.get('https://www.baidu.com/')
        self.browser.implicitly_wait(5)
        self.browser.maximize_window()

    def test_open_baidu_search_bag(self):
        self.browser.find_element_by_css_selector('.s_ipt').send_keys(u'bag')
        sleep(2)
        input_text = self.browser.find_element_by_css_selector('.s_ipt')
        try:
            input_text.clear()
        except Exception as e:
            print(e)
            print(u'清除失败')

        sleep(2)
        self.browser.find_element_by_css_selector('.s_btn').click()
        sleep(3)
        assert True

    def test_open_baidu_search_python(self):
        self.browser.find_element_by_css_selector('.s_ipt').send_keys(u'python')
        self.browser.find_element_by_css_selector('.s_btn').click()
        sleep(3)
        assert True

    def teardown_class(self):
        print(u'退出浏览器')
        self.browser.quit()


if __name__ == '__main__':
    pytest.main(['ui_test.py', '-s'])
