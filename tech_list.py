#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time  


driver = webdriver.Chrome()   #PhantomJS()    #Chrome()   #PhantomJS()

url = 'https://www.youtube.com/results?sp=CAMSAggDUBQ%253D&search_query=music'

driver.get(url)

time.sleep(1)
driver.maximize_window()
#assert "Python" in driver.title
#driver.find_element_by_name('search_query').clear()
#driver.find_element_by_name('search_query').send_keys('music')
#driver.find_element_by_name('search_query').submit()

time.sleep(3)
cnt = 0

for i in range(200):
    js="var q=document.documentElement.scrollTop=%d" % (50*i)
    driver.execute_script(js)
    time.sleep(0.01)

js="var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
time.sleep(2)

cnt = 0

videos = driver.find_elements_by_tag_name('a')
#limit = 2000

fd = open('music.txt', 'w')


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
        
        
        #video.click()
        #time.sleep(2)
        #driver.back()
        #js="var q=document.documentElement.scrollTop=%d" % (cnt*150 + 300)
        #driver.execute_script(js)
        #time.sleep(3)
        #videos = driver.find_elements_by_tag_name('a')
    #if cnt > limit: 
    #    break



#elem.send_keys(Keys.RETURN)
#print driver.page_source

#try: 
#    WebDriverWait(driver, 10).until(lambda driver : driver.title.lower().startswith("!"))
#    print driver.title  

time.sleep(3)
#

#finally:

#time.sleep(3)
driver.quit()

fd.close()
