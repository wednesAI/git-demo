# -*- coding: utf-8 -*-
# @Time : 2020/9/5 14:38
# @Author : wednes
# @File : pythondemo.py
from selenium import webdriver
import time
import unittest
from HTMLReport import addImage
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchWindowException
from selenium.webdriver.common.by import By

class test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    """
    窗口跳转
    """
    def test_switch(self):
        self.driver.get('https://www.baidu.com/')
        # 获取当前窗口句柄
        first_handle = self.driver.current_window_handle
        print('百度首页句柄:', first_handle)
        # 百度搜索框输入selenium并点击百度一下
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        time.sleep(3)
        # 点击selenium的百度百科连接,打开新的窗口
        # partial:部分的,如果是find_element_by__link_text()必须完全匹配
        self.driver.find_element_by_partial_link_text('百度百科').click()
        # 获取所有窗口的句柄
        all_handles = self.driver.window_handles
        print('当前浏览器已经打开的窗口句柄序列:', all_handles)
        # 打印新窗口的句柄
        print('跳转到新的窗口,句柄是:', self.driver.window_handles[-1])
        for handle in all_handles:
            # 切换到新的窗口
            if handle != first_handle:
                self.driver.switch_to.window(handle)
                self.driver.find_element_by_link_text('元素硒的英文名').click()
                # 返回到原来的窗口
                self.driver.switch_to.window(first_handle)
                sendKeys = self.driver.find_element_by_id('kw')
                sendKeys.clear()
                sendKeys.send_keys('python')
    """
    下拉选择
    """
    # def test_select(self):
    #     self.driver.get(r'file:///D:/github demo/WebdriverAPI-master/actionselect.html')
    #     select_element = Select(self.driver.find_element_by_xpath('//select'))
    #     # 找到所有的下拉选项
    #     actual_options = select_element.options
    #     # 期望列表
    #     expect_optionslist = ['桃子', '西瓜', '橘子', '猕猴桃', '山楂', '荔枝']
    #     # 获取所有的选项的文本值
    #     """
    #     map()函数:会根据提供的函数对指定序列做映射,用法map(function, iterable, ...)
    #     def square(x):   # 计算平方数
    #         return x ** 2
    #     map(square, [1,2,3,4,5])   # 计算列表各个元素的平方 >>> [1, 4, 9, 16, 25]
    #     map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数  >>> [1, 4, 9, 16, 25]
    #     """
    #     actual_optionslist = [actual_options for actual_options in map(lambda option: option.text, actual_options)]
    #     print(actual_optionslist)
    #     # 断言
    #     self.assertListEqual(expect_optionslist, actual_optionslist,msg='测试失败时打印的信息')
    """
    单选按钮
    """
    # def test_Radio(self):
    #     import time
    #     self.driver.get(r'file:///D:/github demo/WebdriverAPI-master/radio.html')
    #     # 定位到草莓选项
    #     time.sleep(2)
    #     berry = self.driver.find_element_by_xpath("//input[@value='berry']")
    #     berry.click()
    #     # 断言是否被选中
    #     self.assertTrue(berry.is_selected(),msg='测试失败时打印的信息')
    #
    #     if berry.is_selected():
    #         # 如果被选中了重新选择西瓜选项
    #         watermelon = self.driver.find_element_by_xpath("//input[@value='watermelon']")
    #         watermelon.click()
    #         # 断言草莓未被选中
    #         self.assertFalse(berry.is_selected(),msg='测试失败时打印的信息')
    #         # 查找所有的选项
    #         options = self.driver.find_elements_by_xpath("//input[@name='fruit']")
    #         # 遍历所有的选项，如果找到orange且未被选中，那么就选中这项
    #         for option in options:
    #             if option.get_attribute('value') == 'orange':
    #                 if not option.is_selected():
    #                     option.click()
    """
    多选框
    """
    # def test_CheckBox(self):
    #     self.driver.get(r'file:///D:/github demo/WebdriverAPI-master/checkbox.html')
    #     # 选中一个选项并取消
    #     berry = self.driver.find_element_by_xpath("//input[@value='berry']")
    #     berry.click()
    #     # 断言是否被选中
    #     self.assertTrue(berry.is_selected(),msg='测试失败时打印的信息')
    #     # 取消选中
    #     if berry.is_selected():
    #         berry.click()
    #     # 遍历所有的选项并选中所有的选项
    #     options = self.driver.find_elements_by_xpath("//input[@name='fruit']")
    #     for option in options:
    #         if not option.is_selected():
    #             option.click()

# 判断一个元素是否存在，如何判断alert弹窗出来了，如何判断动态的元素等等一系列的判断，
# 在selenium的expected_conditions模块收集了一系列的场景判断方法
# 网址:https://www.cnblogs.com/adolfmc/p/12640265.html
    """
    ajax
    """
    # def test_AjaxBykeys(self):
    #     '''
    #     在ajax方式产生的悬浮框中，单击选择包含某个关键字的选项
    #     '''
    #     self.driver.get('https://www.sogou.com')
    #     query = self.driver.find_element_by_xpath("//input[@id='query']")
    #     query.send_keys('python')
    #     time.sleep(2)
    #     # 向下选择第三个选项(不能动鼠标到悬浮框,否则从当前鼠标选中开始,)
    #     for i in range(3):
    #         query.send_keys(Keys.DOWN)
    #         time.sleep(1)
    #     query.send_keys(Keys.ENTER)
    """
    杀进程
    """
    # def test_killWindowProcess(self):
    #     """ 杀进程 """
    #     self.driver.get('http://www.baidu.com')
    #     recode = os.system('taskkill /iM chrome.exe /F') # 会结束所有一打开的浏览器的进程
    #     if recode == 0:
    #         print('结束Chrome进程成功')
    #     else:
    #         print('结束浏览器进程失败')

if __name__ == "__main__":
    unittest.main()
