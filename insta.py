import time
import requests
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# chrome에서 F11을 눌러 전체 화면으로 넓히는 옵션입니다.
#options.add_argument('--kiosk')
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# executable_path에는 chromedriver 실행 파일의 경로를 넣고, chrome_options에는 options 변수를 넣습니다.
driver = webdriver.Chrome(executable_path='C:\dev\chromedriver.exe',options=options)

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
time.sleep(5)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(5)


driver.find_element_by_class_name('aOOlW.HoLwm').click()
time.sleep(5)

driver.find_element_by_class_name('XTCLo.x3qfX').send_keys('carstagram')
time.sleep(5)

driver.find_element_by_class_name('z556c').click()
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, parser='html.parser')

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
    soup = BeautifulSoup(html, parser="html.parser")
    imgs=soup.select('div.Nnq7C.weEfm img')
    for i in range(len(imgs)):
        src=imgs[i].attrs['src']
        
        if src not in imglist:
            urllib.request.urlretrieve(src,"./car_img/"+'car{}.png'.format(cnt))
            cnt+=1
            imglist.append(imgs[i].attrs['src'])

    # Calculate new scroll height and compare with last scroll height            
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height==last_height: break
    last_height = new_height

    

# 크롬드라이버 닫기
driver.close()