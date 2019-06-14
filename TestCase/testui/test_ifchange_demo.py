
from Common.baseui import *
from selenium.webdriver import ActionChains
from selenium import webdriver

class TestFirstDemo:

    def test_demo1(self, driver):
        base = baseUI(driver)
        # 打开网址
        base.driver.get("http://www.testing2.ifchange.com/")
        # 点击登录
        base.click("点击页面的登录", '//a[contains(text(),"登录")]')
        # 输入用户名
        base.send_keys("输入用户名", "//input[@placeholder='请输入登录邮箱']", 'chenyang@ifchange.com')
        # 输入密码
        base.send_keys('输入密码', '//input[@placeholder="请输入登录密码"]', 'abc123')
        # 点击登录
        time.sleep(2)
        base.click('登录', "//span[text()='登录']/parent::button")
        time.sleep(2)
        # 切换网址至人才库
        base.driver.get("http://www.testing2.ifchange.com/archives/crm/list")
        time.sleep(5)
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
        driver = webdriver(driver)
        base.driver.get("https://www.ifchange.com/")
        # 点击登录
        base.click("点击页面的登录", '//a[contains(text(),"登录")]')
        # 输入用户名
        base.send_keys("输入用户名", "//input[@placeholder='请输入登录邮箱']", 'baolong.yang@ifchange.com')
        # 输入密码
        base.send_keys('输入密码', '//input[@placeholder="请输入登录密码"]', '20190302aits')
        # 点击登录
        time.sleep(2)
        base.click('登录', "//span[text()='登录']/parent::button")
        time.sleep(2)
        # 切换网址至人才库
        base.driver.get("https://www.ifchange.com/archives/")
        time.sleep(2)
        # 点击展开筛选
        base.click("展开筛选项", '//span[contains(text(),"展开筛选")]')
        # 输入姓名“丁潇潇”
        base.send_keys("输入要搜索的姓名", '//input[@placeholder="请输入姓名"]', "于潇潇")
        time.sleep(5)
        # 鼠标事件回车 或者点击姓名输入框的“√”
        # driver.find_element_by_xpath('//input[@placeholder="请输入姓名"]').send_keys()
        # 点击丁潇潇姓名，或者点击头像进入简历详情页
        #