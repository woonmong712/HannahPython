#1. CGV가 아닌 다른 웹 페이지를 대상으로 자동화 테스트 시나리오를 작성하기.
#2. 자동화 테스트 시나리오를 원하는 도구를 이용해 엑셀 등 파일에 TC화 하기.
#3. TC를 Selenium으로 자동화 하기.
#4. 작성한 시나리오와 TC파일, 자동화 코드 파일을 과제 진행 시 어려웠던 점과 함께 작성하여 제출하기.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# TC_01. 홈페이지 접속
driver.get('https://www.aladin.co.kr/home/welcome.aspx')
if (driver.current_url == "https://www.aladin.co.kr/home/welcome.aspx"):
    print('홈페이지 접속 성공\nTC_01 : PASS')
else:
    print('홈페이지 접속 실패\nTC_01 : FAIL')
    print(driver.current_url)

driver.implicitly_wait(10)

# TC_02. 비유효한 도서명 검색
book_title_01 = 'ㅁㄴㅇ런이ㅏ러 ㅁ'
search_box = driver.find_element(By.CSS_SELECTOR,'#SearchWord')
search_box.click()
search_box.send_keys(book_title_01)
driver.find_element(By.CLASS_NAME,'search_btn').click()

check_text = f"'{book_title_01}'에 대한 검색 결과가 없습니다."
search_result_01 = driver.find_element(By.CSS_SELECTOR,'#wa_SearchResult_wa_search3_Result1_wa_search3_Result_NoResult1_panDefault > div > div.ss_line > table > tbody > tr > td > div')
if (check_text == search_result_01.text):
    print('비유효한 도서명 검색 성공\nTC_02 : PASS')
else:
    print('비유효한 도서명 검색 실패\nTC_02 : FAIL')
    print(search_result_01)

time.sleep(3)

# TC_03. 유효한 도서명 검색 (한글)
book_title_02 = '오래 준비해온 대답'
search_box = driver.find_element(By.CSS_SELECTOR,'#SearchWord')
search_box.click()
search_box.clear()
search_box.send_keys(book_title_02)
driver.find_element(By.CLASS_NAME,'search_btn').click()

search_result_02 = driver.find_element(By.CSS_SELECTOR,'#Search3_Result > div:nth-child(1) > table > tbody > tr > td:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > ul > li:nth-child(1) > a.bo3')
if (book_title_02 == search_result_02.text):
    print('유효한 도서명(한글) 검색 성공\nTC_03 : PASS')
else:
    print('유효한 도서(한글) 검색 실패\nTC_03 : Fail')
    print(search_result_02.text)

time.sleep(3)

# TC_04. 유효한 도서명 검색 (영어)
book_title_03 = 'The Little Prince'
search_box = driver.find_element(By.CSS_SELECTOR,'#SearchWord')
search_box.click()
search_box.clear()
search_box.send_keys(book_title_03)
driver.find_element(By.CLASS_NAME,'search_btn').click()

search_result_03 = driver.find_element(By.CSS_SELECTOR,'#Search3_Result > div:nth-child(1) > table > tbody > tr > td:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > ul > li:nth-child(2) > a')
if (book_title_03 == search_result_03.text):
    print('유효한 도서명(한글) 검색 성공\nTC_04 : PASS')
elif book_title_03 in search_result_03.text:
    print('유효한 도서명(한글) 검색 성공\nTC_04 : PASS')
    print(search_result_03.text)
else:
    print('유효한 도서(한글) 검색 실패\nTC_04 : Fail')
    print(search_result_03.text)

time.sleep(3)

# TC_05. 특수문자 포함 음반 검색
music_title_01 = '[미니 CD]'
search_box = driver.find_element(By.CSS_SELECTOR,'#SearchWord')
search_box.click()
search_box.clear()
search_box.send_keys(music_title_01)
driver.find_element(By.CLASS_NAME,'search_btn').click()

search_result_04 = driver.find_element(By.CSS_SELECTOR,'#Search3_Result > div:nth-child(1) > table > tbody > tr > td:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > ul > li:nth-child(1) > a.bo3')
if (music_title_01 == search_result_04.text):
    print('특수문자 포함된 음반명 검색 성공\nTC_05 : PASS')
elif music_title_01 in search_result_04.text:
    print('특수문자 포함된 음반명 검색 성공\nTC_05 : PASS')
    print(search_result_04.text)
else:
    print('유효한 도서(한글) 검색 실패\nTC_05 : Fail')
    print(search_result_04.text)

time.sleep(3)

# TC_06. 검색한 음반 클릭하여 상세 페이지 접속
driver.find_element(By.CSS_SELECTOR,'#Search3_Result > div:nth-child(1) > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(1) > td > div > a > img').click()
result_text = driver.find_element(By.CSS_SELECTOR,'#Ere_prod_allwrap > div.Ere_prod_bookwrap > div.Ere_prod_Binfowrap > div > div:nth-child(1) > ul > li:nth-child(1) > div.Litem')
check_text = '판매가'

if (check_text == result_text.text):
    print('특수문자 포함된 음반명 검색 성공\nTC_06 : PASS')
else:
    print('유효한 도서(한글) 검색 실패\nTC_06 : Fail')
    print(result_text.text)

# TC_07. 알라딘 로고 버튼 기능 확인
driver.find_element(By.CSS_SELECTOR,'#logoBtn > img').click()
if (driver.current_url == "https://www.aladin.co.kr/home/welcome.aspx"):
    print('홈페이지 접속 성공\nTC_07 : PASS')
else:
    print('홈페이지 접속 실패\nTC_07 : FAIL')
    print(driver.current_url)

# 위치 이동
driver.execute_script("window.scrollTo(0,500)")
time.sleep(3)