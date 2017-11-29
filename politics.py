#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
import time  

cnt = 0
fd = open('sports.txt', 'r')
res = open('sports_result.txt', 'w')
res.writelines('MUSIC TEST\n') 
res.writelines(time.strftime('%Y-%m-%d %H:%M:%S\n', time.localtime(time.time())))
res.writelines(' No |                Title                |   Views   |  Comments  |  Likes  | Dislikes | Subscribers |  Post Date  \n') 


while 1:
    res_str = ''
    url = fd.readline()
    if not url:
        break
    driver = webdriver.Chrome()   #PhantomJS()
    
    cnt = cnt + 1
    tmp = str(cnt)
    res_str = res_str + tmp + ' | '
    driver.get(url)
    time.sleep(2)
    driver.maximize_window()

#assert "Python" in driver.title
#driver.find_element_by_name('search_query').clear()
#driver.find_element_by_name('search_query').send_keys('history')
#driver.find_element_by_name('search_query').submit()
#driver.find_element_by_partial_link_text("Inside Politics").click()

# simulate scroll down action to grab data below the page, we need to record the page source within the process
# otherwise the page would go up again, and the source page would not record data below
    js="var q=document.documentElement.scrollTop=%d" % (550)
    driver.execute_script(js)
    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    time.sleep(2)
    js="var q=document.documentElement.scrollTop=0"
    driver.execute_script(js)
    time.sleep(0.1)
#print(html)


    print 'The video title is:', driver.title
    res_str = res_str + driver.title + ' | ' 

    view_infos = soup.select('div#count > yt-view-count-renderer')
    for info in view_infos:
        view = info.find('span', class_ = 'view-count style-scope yt-view-count-renderer').text 
        res_str = res_str + view[:-6] + ' | '
        print 'Number of views:', view[:-6]


    comments_infos = soup.select('#count > yt-formatted-string.count-text.style-scope.ytd-comments-header-renderer')
    for info in comments_infos:
        res_str = res_str + info.text[:-9] + ' | '
        print 'Number of comments:', info.text[:-9]
    

    like_infos = soup.select('yt-formatted-string#text')
    i = 1
    for info in like_infos:
        if info.text == 'Sign in' or info.text == 'Find out why' or info.text == 'Share':
            continue
        elif i == 1: 
            likes = info.text
            res_str = res_str + likes + ' | '
            print 'Number of likes:', likes
        elif i == 2:
            dislikes = info.text
            res_str = res_str + dislikes + ' | '
            print 'Number of dislikes:', dislikes
        elif i == 3:
            subs = info.text[10:]
            res_str = res_str + subs + ' | '
            print 'Number of subscribers:', subs
    
        i = i + 1


    post_infos = soup.select('#upload-info > span.date.style-scope.ytd-video-secondary-info-renderer') 
#meta > meta-contents > ytd-video-secondary-info-renderer > ytd-video-owner-renderer') #.style-scope ytd-video-owner-renderer')
    for info in post_infos:
        print 'Post date:', info.text[13:]
        res_str = res_str + info.text[13:] + '\n'

    print(res_str)
    res.writelines(res_str)
    
    time.sleep(2)
    driver.quit()


fd.close()
res.close()
