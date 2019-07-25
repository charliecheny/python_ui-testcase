
from Common.baseui import *
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import random
import re

class TestFirstDemo:
    #
    # def tes1t_demo1(self, driver):
    #     base = baseUI(driver)
    #     # 打开网址
    #     base.driver.get("http://www.testing2.ifchange.com/")
    #     # 点击登录
    #     base.click("点击页面的登录", '//a[contains(text(),"登录")]')
    #     # 输入用户名
    #     base.send_keys("输入用户名", "//input[@placeholder='请输入登录邮箱']", 'chenyang@ifchange.com')
    #     # 输入密码
    #     base.send_keys('输入密码', '//input[@placeholder="请输入登录密码"]', 'abc123')
    #     # 点击登录
    #     time.sleep(2)
    #     base.click('登录', "//span[text()='登录']/parent::button")
    #     time.sleep(2)
    #     # 切换网址至人才库
    #     base.driver.get("http://www.testing2.ifchange.com/archives/crm/list")
        # time.sleep()
        # 点击新增任务
        # 点击发送生日祝福
        # 输入任务名称;儿童节快乐
        # 点击邮件模板下拉框
        # 点击：节日祝福--系统模板
        # 点击推送职位下拉框
        # 点击职位 测试啦啦啦[上海] 东方时尚[成都市]
        # 点击确定按钮
        # 点击请选择上传文件夹
        # 点击创建文件夹
        # 输入文件夹名字
        # 点击确定
        # 点击选择职能 软件测试 项目经理
        # 点击确定
        # 点击下一步

    def test_resume_detail(self, driver):
        base = baseUI(driver)
        # 打开网址
        base.driver.get("https://www.ifchange.com/")
        print(base.get_the_title())
        # 点击登录
        base.click("点击页面的登录", '//a[contains(text(),"登录")]')
        # 输入用户名
        base.send_keys("输入用户名", "//input[@placeholder='请输入登录邮箱']", 'baolong.yang@ifchange.com')
        # 输入密码
        base.send_keys('输入密码', '//input[@placeholder="请输入登录密码"]', '20190619aits')
        # 点击登录
        base.click('登录', "//span[text()='登录']/parent::button")
        # 切换网址至人才库
        base.driver.get("https://www.ifchange.com/archives/")
        time.sleep(2)
        # 点击展开筛选
        base.click("展开筛选项", '//span[contains(text(),"展开筛选")]')
        # 输入姓名“马骏”
        base.send_keys("输入要搜索的姓名", '//input[@placeholder="请输入姓名"]', "马骏")
        # 鼠标事件回车 或者点击姓名输入框的“√”
        base.keys_enter("点击回车搜索", '//input[@placeholder="请输入姓名"]')
        time.sleep(3)
        # 点击马骏姓名，或者点击头像进入简历详情页
        base.click("定位到第一个马骏", "(//span[contains(text(),'马骏')])[2]")
        # 判断当前的title是否是“我的人才_e成”
        ec_title_contains = EC.title_contains("我的人才_e成")
        print(ec_title_contains(driver))
        time.sleep(2)

        # 判断简历详情页的数据是否和预期的一样
        # 判断简历详情页里的设置优先展示原始简历还是标准简历的确定按钮是否存在
        if base.displayed("//span[contains(text(),'确定')]/parent::button"):
            # print("element is true")
            if base.displayed("//span[contains(text(),'优先展示标准简历')]"):
                # print("element2 is true")
                base.click("点击优先展示标准简历", "//span[contains(text(),'优先展示标准简历')]")
                base.click("点击展示标准简历", "//span[contains(text(),'确定')]/parent::button")
                base.click("点击标准简历", "//li[text()='标准简历']")
            else:
                base.click("点击标准简历", "//li[text()='标准简历']")
        else:
            base.click("点击标准简历", "//li[text()='标准简历']")
        print(base.displayed("//span[contains(text(),'18298489023')]"))
        print(base.displayed("//span[contains(text(),'1670063424@qq.com')]"))
        print(base.displayed("//div[contains(text(),'求职意向')]"))
        print(base.displayed("//div[contains(text(),'教育经历')]"))
        print(base.displayed("//div[contains(text(),'工作经历')]"))

    def test_random_resume_detail(self, driver):
        # a_list = []
        base = baseUI(driver)
        # 打开网址
        base.driver.get("https://www.ifchange.com/")
        # # 点击登录
        # base.click("点击页面的登录", '//a[contains(text(),"登录")]')
        # # 输入用户名
        # base.send_keys("输入用户名", "//input[@placeholder='请输入登录邮箱']", 'baolong.yang@ifchange.com')
        # # 输入密码
        # base.send_keys('输入密码', '//input[@placeholder="请输入登录密码"]', '20190619aits')
        # # 点击登录
        # base.click('登录', "//span[text()='登录']/parent::button")
        # 切换网址至人才库
        base.driver.get("https://www.ifchange.com/archives/")
        time.sleep(3)
        # 获取所有包含简历详情的a标签
        # element = base.find_elements_xpath("//span[text()='全选']/parent::label/parent::div/parent::div/parent::div//following-sibling::div//a")
        element = base.find_elements_xpath('//div[@class="ic-layoutnew__content-wrap"]//div[@class="ant-spin-nested-loading"]//div[@class="resume__item"]//a')
        # 获取元素里的链接
        # for i in element:
        #     link = i.get_attribute("href")
        #     a_list.append(link)
        # base.driver.get(a_list[a])
        choice = random.choice(element)
        choice.click()
        # 判断简历详情页的数据是否和预期的一样
        # 判断简历详情页里的设置优先展示原始简历还是标准简历的确定按钮是否存在
        if base.displayed("//span[contains(text(),'确定')]/parent::button"):
            # print("element is true")
            if base.displayed("//span[contains(text(),'优先展示标准简历')]"):
                # print("element2 is true")
                base.click("点击优先展示标准简历", "//span[contains(text(),'优先展示标准简历')]")
                base.click("点击展示标准简历", "//span[contains(text(),'确定')]/parent::button")
                base.click("点击标准简历", "//li[text()='标准简历']")
            else:
                base.click("点击标准简历", "//li[text()='标准简历']")
        else:
            base.click("点击标准简历", "//li[text()='标准简历']")
        print(base.displayed("//div[contains(text(),'求职意向')]"))
        print(base.displayed("//div[contains(text(),'教育经历')]"))
        print(base.displayed("//div[contains(text(),'工作经历')]"))

    def test_resume_download(self, driver):
        base = baseUI(driver)
        # 打开网址
        base.driver.get("https://www.ifchange.com/")
        print(base.get_the_title())
        # 点击登录
        base.click("点击页面的登录", '//a[contains(text(),"登录")]')
        # 输入用户名
        base.send_keys("输入用户名", "//input[@placeholder='请输入登录邮箱']", 'baolong.yang@ifchange.com')
        # 输入密码
        base.send_keys('输入密码', '//input[@placeholder="请输入登录密码"]', '20190619aits')
        # 点击登录
        base.click('登录', "//span[text()='登录']/parent::button")
        # 切换网址至人才库
        base.driver.get("https://www.ifchange.com/archives/")
        time.sleep(1)
        # 点击跳转任意页
        base.send_keys("输入任意页的值", "//button[text()='确定']/parent::div//input", '11')
        base.click("点击确定", "//button[text()='确定']")
        time.sleep(2)
        # 获取页面所有a标签的链接
        element = base.find_elements_xpath('//div[@class="ic-layoutnew__content-wrap"]//div[@class="ant-spin-nested-loading"]//div[@class="resume__item"]//a')
        # 获取元素里的链接
        # for i in element:
        #     link = i.get_attribute("href")
        #     a_list.append(link)
        # base.driver.get(a_list[a])
        choice = random.choice(element)
        choice.click()
        # time.sleep(2)
        base.click("点击导出为文件", '//div[@class="operation-item export-item"]')
        base.click("点击导出为pdf", '//div[@class="download-icon"]/a[2]')
        time.sleep(2)