#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time  


driver = webdriver.Chrome()   #PhantomJS()    #Chrome()   #PhantomJS()

url = 'http://www.youtube.com'

driver.get(url)

time.sleep(1)
driver.maximize_window()
#assert "Python" in driver.title
driver.find_element_by_name('search_query').clear()
driver.find_element_by_name('search_query').send_keys('history')
driver.find_element_by_name('search_query').submit()

#driver.find_element_by_partial_link_text("Inside Politics").click()
cnt = 0

'''
for i in range(2):
    js="var q=document.documentElement.scrollTop=%d" % (50*i)
    driver.execute_script(js)
    time.sleep(0.01)

js="var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
time.sleep(3)
'''


videos = driver.find_elements_by_tag_name('a')
#limit = 2000

print len(videos)
for video in videos: #driver.find_elements_by_tag_name('a'): 
    if video.get_attribute('id') == 'video-title':
        vname = video.get_attribute('aria-label') 
        #if video.get_attribute('class') == "view-count style-scope yt-view-count-renderer":
           # views = 

        #href_name = video.get_attribute('href')
        cnt = cnt + 1
        print vname, cnt
        video.click()
        views = driver.find_element_by_class_name('view-count style-scope yt-view-count-renderer').text
        time.sleep(2)
        driver.back()
        #js="var q=document.documentElement.scrollTop=%d" % (cnt*150 + 300)
        #driver.execute_script(js)
        #time.sleep(3)
        #videos = driver.find_elements_by_tag_name('a')
    #if cnt > limit: 
    #    break

print(cnt)


#elem.send_keys(Keys.RETURN)
#print driver.page_source


time.sleep(5)
#try: 
#    WebDriverWait(driver, 10).until(lambda driver : driver.title.lower().startswith("!"))
#    print driver.title  
#
print(driver.title)

#finally:

#time.sleep(3)
driver.quit()


