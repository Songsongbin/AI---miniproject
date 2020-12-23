# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv

f=open("파이썬.csv","w", encoding="UTF-8")
# executable_path에는 chromedriver 실행 파일의 경로를 넣고, chrome_options에는 options 변수를 넣습니다.
driver = webdriver.Chrome(executable_path='C:\dev\chromedriver.exe')

url = "http://naver.com"
driver.get(url)
driver.implicitly_wait(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

driver.find_element_by_id('query').send_keys('파이썬')
driver.find_element_by_css_selector('#search_btn').click()

driver.find_element_by_xpath("//*[@id='main_pack']/section[3]/div/div[1]/div/div[1]/a[2]").click()



html = driver.page_source
soup = BeautifulSoup(html, parser="html.parser")
d={}
lists=soup.find_all(class_='lst_total')
for i in range(30):
    
    aa = soup.select('#sp_blog_{}'.format(i+1))
    
    d['{}'.format(i+1)]=("제목: "+aa[0].select('.api_txt_lines.total_tit')[0].text+" URL: "+aa[0].select('.total_dsc')[0].get('href'))
    
    #print(soup.select('#sp_blog_{}'.format(i+1)))
print(d)

for i in d.keys():
    f.write(i +',' + d[i]+'\n')
f.close()

#driver.close()