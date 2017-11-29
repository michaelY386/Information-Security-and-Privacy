#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
import time
import sys


cg = 0

while (1):
    
    if cg == 0:
        fd = open('music.txt', 'r')
        res = open('music_result.txt', 'wt')
        res.write('MUSIC TEST\n') 
    elif cg == 1:
        fd = open('sports.txt', 'r')
        res = open('sports_result.txt', 'wt')
        res.writelines('SPORTS TEST\n') 
    elif cg == 2:
        fd = open('entertainment.txt', 'r')
        res = open('entertainment_result.txt', 'wt')
        res.writelines('ENTERTAINMENT TEST\n') 
    elif cg == 3:
        t = 'politics'
        fd = open('politics.txt', 'r')
        res = open('politics_result.txt', 'wt')
        res.writelines('POLITICS TEST\n') 
    elif cg == 4:
        t = 'technology'
        fd = open('technology.txt', 'r')
        res = open('technology_result.txt', 'wt')
        res.writelines('TECHNOLOGY TEST\n') 
    
    cg = cg + 1
    cnt = 0
    print res
    res.writelines(time.strftime('%Y-%m-%d %H:%M:%S\n', time.localtime(time.time())))
    res.writelines('No |   Views   |  Comments  |  Likes  | Dislikes | Subscribers |  Post Date  \n') 
    
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
        time.sleep(5)
        driver.maximize_window()

# simulate scroll down action to grab data below the page, we need to record the page source within the process
# otherwise the page would go up again, and the source page would not record data below
        js="var q=document.documentElement.scrollTop=%d" % (530)
        driver.execute_script(js)
        time.sleep(5)

        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')

        time.sleep(1)
        js="var q=document.documentElement.scrollTop=0"
        driver.execute_script(js)
        time.sleep(2)
        

        print 'The video title is:', driver.title
        #res_str = res_str + driver.title + ' | ' 

        view_infos = soup.select('div#count > yt-view-count-renderer')
        for info in view_infos:
            view = info.find('span', class_ = 'view-count style-scope yt-view-count-renderer').text 
            res_str = res_str + view[:-6] + ' | '
            print 'Number of views:', view[:-6]


        comments_infos = soup.select('#count > yt-formatted-string.count-text.style-scope.ytd-comments-header-renderer')
        if (len(comments_infos) == 0):
            res_str = res_str + ' No comments available  |'
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
        for info in post_infos:
            print 'Post date:', info.text[13:]
            res_str = res_str + info.text[13:] + '\n'

        res_str = res_str + '\n'
        print(res_str)
        res.write(res_str)
    
        time.sleep(1)
        driver.quit()
           
    fd.close()
    res.close()

    if cg == 5:
        break
