#!/usr/bin/env python
# coding=utf-8
from selenium import webdriver
 
driver = webdriver.PhantomJS()
driver.set_page_load_timeout(5)
driver.get('http://www.baidu.com')
try:
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw')  # 通过ID定位
    driver.find_element_by_class_name('s_ipt')  # 通过class属性定位
    driver.find_element_by_name('wd')  # 通过标签name属性定位
    driver.find_element_by_tag_name('input')  # 通过标签属性定位
    driver.find_element_by_css_selector('#kw')  # 通过css方式定位
    driver.find_element_by_xpath("//input[@id='kw']")  # 通过xpath方式定位
    driver.find_element_by_link_text("贴吧")  # 通过xpath方式定位
    print(driver.find_element_by_id('kw').tag_name ) # 获取标签的类型
except Exception as e:
    print(e)
driver.quit()
