import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# chrome에서 F11을 눌러 전체 화면으로 넓히는 옵션입니다.
options.add_argument('--kiosk')

# executable_path에는 chromedriver 실행 파일의 경로를 넣고, chrome_options에는 options 변수를 넣습니다.
driver = webdriver.Chrome(executable_path='C:\dev\chromedriver.exe', chrome_options=options)

url = "http://daum.net"
driver.get(url)
driver.implicitly_wait(3)

# 로그인버튼
driver.find_element_by_css_selector('#inner_login > a:nth-child(1)').click()
time.sleep(2)

# 아이디
driver.find_element_by_id('id').send_keys('whdgh03')
time.sleep(2)

# 비밀번호
driver.find_element_by_name('pw').send_keys('rkddml3#')
time.sleep(2)

# 로그인시도
driver.find_element_by_css_selector('.btn_comm').click()
time.sleep(2)

# 메일 버튼
# driver.find_element_by_xpath('//*[@id="mArticle"]/div[1]/div[2]/ul/li[1]/a').click()
driver.find_element_by_class_name('link_basis').click()
time.sleep(2)

# 메일쓰기
driver.find_element_by_xpath('//*[@id="daumHead"]/div[1]/button[1]').click()
time.sleep(2)

# 받는사람
to = driver.find_element_by_xpath('//*[@id="toTextarea"]')
to.send_keys('whdgh03@hanmail.net')
time.sleep(3)

# 글 제목
title = driver.find_element_by_xpath('//*[@id="mailSubject"]')
title.click()
time.sleep(2)

title.send_keys('메일 제목입니다.')
time.sleep(2)

# iframe 들어가기
driver.switch_to_frame('tx_canvas_wysiwyg')
time.sleep(2)

# 메일 글내용
driver.find_element_by_xpath('/html/body').send_keys('안녕하세요')
time.sleep(2)

# iframe 나가기
driver.switch_to_default_content()
time.sleep(2)

# 보내기 버튼
driver.find_element_by_xpath('//*[@id="composer"]/div/div[1]/div[2]/div/div/button[1]').click()
time.sleep(2)

# 크롬드라이버 닫기
driver.close()