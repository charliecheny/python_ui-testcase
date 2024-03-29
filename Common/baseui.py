#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time


import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

def shot(func):
    def function(*args, **kwargs):
        allure.attach(args[0].driver.get_screenshot_as_png(), args[1] + '之前', allure.attachment_type.PNG)

        res = func(*args, **kwargs)
        allure.attach(args[0].driver.get_screenshot_as_png(), args[1] + '之后', allure.attachment_type.PNG)
        return res
    return function


class baseUI():

    def __init__(self,driver):
        self.driver = driver



    def local_element(self,xpath):
       return WebDriverWait(self.driver, 5, 0.3).until(EC.presence_of_element_located((By.XPATH,xpath)))

    def find_elements_xpath(self,xpath):
        # 获取xpath对应的元素列表，返回的是一个列表
        return self.driver.find_elements_by_xpath(xpath)
    @shot
    def send_keys(self,step,xpath,text):
        '''
        文本输入框清空并填值
        :param step:操作步骤
        :param xpath: xpath
        :param text: 填的值
        :return:
        '''
        element = self.local_element(xpath)
        element.clear()
        element.send_keys(text)


    @shot
    def click(self,step,xpath):
        '''
        #点击操作
        :param step: 操作步骤
        :param xpath: xpath
        :return:
        '''
        element = self.local_element(xpath)
        element.click()
    @shot
    def scroll_screen(self,step):
        '''
        #滚动窗口，滚到底
        :param step:操作步骤
        :return:
        '''
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
    @shot
    def switch_to_frame(self,step,xpath):
        '''
        #切换到iframe里边
        :param step:操作步骤
        :param xpath: xpath
        :return:
        '''
        element = self.local_element(xpath)
        self.driver.switch_to.frame(element)
    @shot
    def switch_to_content(self,step):
        '''
        #切出iframe，回到默认页面
        :param step:操作步骤
        :return:
        '''
        self.driver.switch_to.default_content()

    @shot
    def select_by_index(self,step,xpath,index):
        '''
        #操作select下拉框，通过下标选择
        :param step:操作步骤
        :param xpath:xpath
        :param index:下标
        :return:
        '''
        element = self.local_element(xpath)
        Select(element).select_by_index(index)

    @shot
    def select_by_value(self,step,xpath,value):
        '''
        #操作select下拉框，通过value值选择
        :param step: 操作步骤
        :param xpath: xpath
        :param value: value值
        :return:
        '''
        element = self.local_element(xpath)
        Select(element).select_by_value(value)

    @shot
    def select_by_visible_text(self,step,xpath,text):
        '''
        #操作select下拉框，通过可视文本值选择
        :param step:操作步骤
        :param xpath:xpath
        :param text:可视文本
        :return:
        '''
        element = self.local_element(xpath)
        Select(element).select_by_visible_text(text)

    @shot
    def switch_to_windows_by_title(self,step,title):
        '''
        #切换到名字为title的窗口
        :param step: 操作步骤
        :param title: 窗口标题
        :return: 返回值：当前窗口的句柄
        '''
        current=self.driver.current_window_handle
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to_window(handle)
            if(self.driver.title.__contains__(title)):
                break
        return current

    @shot
    def switch_to_alert_accept(self,step):
        '''
        #窗口切换至弹窗并确认
        :param step:操作步骤
        :return:
        '''
        try:
            WebDriverWait(self.driver, 5, 0.5).until(EC.alert_is_present)
        except:
            print('弹框不存在')
            raise
        self.driver.switch_to_alert()
        self.driver.switch_to_alert().accept()

    @shot
    def switch_to_atert_dismiss(self,step):
        '''
        #窗口切换至弹窗并取消
        :param step:操作步骤
        :return:
        '''
        try:
            WebDriverWait(self.driver, 5, 0.5).until(EC.alert_is_present)
        except:
            print('弹框不存在')
            raise
        self.driver.switch_to_alert()
        self.driver.switch_to_alert().dismiss()

    @shot
    def switch_to_alert_send_keys(self,step,text):
        '''
        #窗口切换至弹窗输入内容并确定
        :param step: 操作步骤
        :param text: 输入的文本
        :return:
        '''

        try:
            WebDriverWait(self.driver, 5, 0.5).until(EC.alert_is_present)
        except:
            print('弹框不存在')
            raise
        self.driver.switch_to_alert()
        alert = self.driver.switch_to_alert()
        alert.send_keys(text)
        alert.accept()

    @shot
    def forward(self,step):
        '''
        #导航栏操作，前进
        :param step: 操作步骤
        :return:
        '''
        self.driver.forward()

    @shot
    def back(self,step):
        '''
        #导航栏操作，后退
        :param step:
        :return:
        '''
        self.driver.back()

    @shot
    def refresh(self,step):
        '''
        #导航栏操作，刷新
        :param step: 操作步骤
        :return:
        '''
        self.driver.refresh()


    def execute_script(self,js):
        self.driver.execute_script(js)


    def double_to_single_mark(self,s):
        return s.replace('"','\'')

    @shot
    def update_attribute_by_xpath(self,step,xpath,attribute_name,attribute_value):
        '''
        #通过xpath根据修改html标签属性的值
        :param step: 操作步骤
        :param xpath: xpath
        :param attribute_name:属性名
        :param attribute_value: 属性值
        :return:
        '''
        try:
            self.local_element(xpath)
            js = "var xpath = \"" + self.double_to_single_mark(
            xpath) + "\";var element = document.evaluate(xpath,document,null,XPathResult.ANY_TYPE,null).iterateNext();element.setAttribute(\"" + attribute_name + "\",\"" + attribute_value + "\");"
            self.execute_script(js)
        except:
            print("修改属性值失败，属性名:" + attribute_name + " 属性值:" + attribute_value)
            raise

    @shot
    def remove_attribute_by_xpath(self,step,xpath,attribute_name):
        '''
        #通过xpath删除html标签属性
        :param step:操作步骤
        :param xpath:xpath
        :param attribute_name:属性名
        :return:
        '''
        try:
            self.local_element(xpath)
            js = "var xpath = \"" + self.double_to_single_mark(
                xpath) + "\";var element = document.evaluate(xpath,document,null,XPathResult.ANY_TYPE,null).iterateNext();element.removeAttribute(\"" + attribute_name + "\");"
            self.execute_script(js)
        except:
            print("修改属性值失败，属性名:" + attribute_name)
            raise
    @shot
    def move_to_element(self,step,xpath):
        '''
        #窗口滚动到指定的元素
        :param step: 操作步骤
        :param xpath: xpath
        :return:
        '''
        ActionChains(self.driver).move_to_element(self.local_element(xpath)).perform()
    @shot
    def get_text(self,step,xpath):
        '''
        #获取元素的展示文本
        :param step:操作步骤
        :param xpath:xpath
        :return:页面元素的展示文本
        '''

        element=self.local_element(xpath)

        return element.text
    def get_page_source(self):
        '''
        # 获取页面源码
        :return:页面元素的展示文本
        '''
        return self.driver.page_source
    def real_is_displayed(self,step,xpath):
        '''
        # 判断元素是否存在,只能判断隐藏的元素和已存在的元素,不能在不存在的元素上调用is_displayed()方法
        :param step:操作步骤
        :param xpath:xpath
        :return: 存在返回True,不存在返回False
        '''
        return self.driver.find_element_by_xpath(xpath).is_displayed()
    def displayed(self,xpath):
        # 判断页面的元素是否存在，存在返回True,不存在返回False
        found = False
        while not found:
            try:
                element_ = self.driver.find_element_by_xpath(xpath)
                # if element_.is_displayed():
                    # value = element_.find_element_by_css_selector("*")
                    # print("Element: " + value.text)
                found = True
            except NoSuchElementException:
                time.sleep(1)
                # print("Element: N/A")
                # found = False
                return False
        return found
    def get_the_title(self):
        # 获取title
        # 注意点：这里的title不能加括号，可以链接进去看其调用方法
        title = self.driver.title
        return title
    @shot
    def get_tag_name(self,step,xpath):
        '''
        #获取元素标签
        :param step:操作步骤
        :param xpath:xpath
        :return:页面元素标签
        '''

        element=self.local_element(xpath)
        return element.tag_name
    @shot
    def get_other_attribute(self,step,xpath,attribute):
        '''
        #获取元素的其他属性的值,或者文本框输入的值
        :param step:操作步骤
        :param xpath:xpath
        :param attribute:其他属性的值，或者文本框输入的值，例如class，value
        :return:页面元素的展示文本
        '''

        element=self.local_element(xpath)

        return element.get_attribute(attribute)

    def get_name(self):
        # 获取浏览器名称
        return self.driver.name
    @shot
    def keys_enter(self, step, xpath):
        '''
        键盘操作 回车操作
        :param step:操作步骤
        :param xpath: xpath
        '''
        element = self.local_element(xpath)
        element.send_keys(Keys.ENTER)

    @shot
    def keys_back_space(self, step, xpath):
        '''
        键盘操作 删除最后一个字符
        :param step:操作步骤
        :param xpath: xpath
        '''
        element = self.local_element(xpath)
        element.send_keys(Keys.BACK_SPACE)

    @shot
    def keys_tab(self, step, xpath):
        '''
        键盘操作 tab键
        :param step:操作步骤
        :param xpath: xpath
        '''
        element = self.local_element(xpath)
        element.send_keys(Keys.TAB)

    @shot
    def keys_space(self, step, xpath):
        '''
        键盘操作 空格键
        :param step:操作步骤
        :param xpath: xpath
        '''
        element = self.local_element(xpath)
        element.send_keys(Keys.SPACE)

    @shot
    def keys_escape(self, step, xpath):
        '''
        键盘操作 回退键
        :param step:操作步骤
        :param xpath: xpath
        '''
        element = self.local_element(xpath)
        element.send_keys(Keys.ESCAPE)

    @shot
    def keys_ctrl(self, step, xpath, letter):
        '''
        键盘操作 ctrl加字母
        :param step:操作步骤
        :param xpath: xpath
        :param letter: 键盘按住的字母
        '''
        element = self.local_element(xpath)
        element.send_keys(Keys.CONTROL, letter)



