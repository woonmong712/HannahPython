import time
from selenium import webdriver

driver = webdriver.Chrome()
# 특정 원하는 페이지 진입
driver.get("https://www.naver.com")

# 브라우저 크기 최대로 하기
driver.maximize_window()
time.sleep(3)

# 해당 페이지의 타이틀, URL 출력
print(driver.current_url)
print(driver.title)

# 브라우저 위치 크기 조정
driver.set_window_position(0, 0)
time.sleep(3)
driver.set_window_size(1920, 100)

# # 또 다른 페이지 접속
# driver.get("https://www.google.com")
# print(driver.current_url)
# print(driver.title)
