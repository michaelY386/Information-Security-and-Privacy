#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time  

i = 0

while (1):
    driver = webdriver.Chrome()   #PhantomJS()    #Chrome()   #PhantomJS()
    print i;
    
    if i == 0:
        tmp = 'music'
    elif i == 1:
        tmp = 'sports'
    elif i == 2:
        tmp = 'entertainment'
    elif i == 3:
        tmp = 'politics'
    elif i == 4:
        tmp = 'technology'

    url = 'https://www.youtube.com/results?sp=CAMSAggDUBQ%253D&search_query=' + tmp
    i = i + 1

    driver.get(url)

    time.sleep(1)
    driver.maximize_window()

    time.sleep(2)
    cnt = 0

    for ii in range(200):
        js="var q=document.documentElement.scrollTop=%d" % (50*ii)
        driver.execute_script(js)
        time.sleep(0.01)

    js="var q=document.documentElement.scrollTop=0"
    driver.execute_script(js)
    time.sleep(2)

    videos = driver.find_elements_by_tag_name('a')
    fdname = tmp + '.txt'
    fd = open(fdname, 'w')

    
    print len(videos)
    for video in videos: #driver.find_elements_by_tag_name('a'): 
        if video.get_attribute('id') == 'video-title':
            vname = video.get_attribute('aria-label') 
            cnt = cnt + 1
            if cnt > 51:
                break
            vhref_name = video.get_attribute('href') 
            print vname, vhref_name, cnt
            vhref_name = vhref_name + '\n'
            fd.writelines(vhref_name)
        
    time.sleep(3)
    driver.quit()
    fd.close()
    if i == 5:
        break

