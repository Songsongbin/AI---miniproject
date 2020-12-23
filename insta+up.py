from io import BytesIO
import time
import requests
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import base64
import pymssql

conn=pymssql.connect(host='14.38.220.222',user='python1',password='python1',database='staging', charset='utf8')
cursor = conn.cursor()  
#cursor.execute("select user_name AS ID,user_level AS LV,champ_name,position,concat(year,'-',month,'-',day,' ',minute,':',second) match_date,color_name from lol_match_detail D join lol_user U on D.fk_lol_user_seq = U.seq join lol_champ C on D.fk_lol_champ_seq= C.seq join lol_match M on D.fk_lol_match_seq = M.seq join lol_team_color T on D.fk_lol_team_color_seq = T.seq;")

 
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
 
createFolder('./img')

#options = Options()
# chrome에서 F11을 눌러 전체 화면으로 넓히는 옵션입니다.
#options.add_argument('--kiosk')

# executable_path에는 chromedriver 실행 파일의 경로를 넣고, chrome_options에는 options 변수를 넣습니다.
driver = webdriver.Chrome(executable_path='C:\dev\chromedriver.exe')

url = "https://www.instagram.com/"
driver.get(url)
driver.implicitly_wait(3)


# 아이디
driver.find_element_by_name('username').send_keys('vv_inee')
time.sleep(2)

# 비밀번호
driver.find_element_by_name('password').send_keys('River981218!')
time.sleep(2)

# 로그인시도
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(2)

driver.find_element_by_class_name('aOOlW.HoLwm').click()
time.sleep (2)

driver.find_element_by_class_name('XTCLo.x3qfX').send_keys('가을바람이차다')
time.sleep(1)

driver.find_element_by_class_name('z556c').click()
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

SCROLL_PAUSE_TIME = 2

last_height = driver.execute_script("return document.body.scrollHeight")        

cnt=0
imglist=[]
while True:
    
    # Scroll down to bottom                                                     
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    '''
    # Wait to load page
                                                   
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);") 
    time.sleep(SCROLL_PAUSE_TIME)
    '''
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    imgs=soup.select('div.Nnq7C.weEfm img')
    for i in range(len(imgs)):
        src=imgs[i].attrs['src']
        
        if src not in imglist:
            urllib.request.urlretrieve(src,"./img/"+'가을{}.png'.format(cnt))
            
            imglist.append(imgs[i].attrs['src'])

            with open('./img/가을{}.png'.format(cnt),'rb') as image_file:
                binary_image=base64.b64encode(image_file.read())

            binary_image=binary_image.decode('UTF-8')

            cursor.execute("INSERT INTO Image_File(STUDENT_NAME,IMAGE_NAME,BASE64,CREATED,UPDATED) VALUES('수빈','{}', '{}',CURRENT_TIMESTAMP,CURRENT_TIMESTAMP);".format('가을'+str(cnt), binary_image))

            cnt+=1
    # Calculate new scroll height and compare with last scroll height            
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height==last_height: break 
    last_height = new_height

    
conn.commit()
# 크롬드라이버 닫기
driver.close()