# try:
# import time
#    if 5/0 >= 1:
#         print("1보다 크다")
#     else:
#         print("1보다 작다")
#     print("계산 종료")
# except Exception as e:
#     print(f"나눗셈 에러 발생!!! >>> {e}")

# print("에러 이후 코드")

# import time
# nowStamp = time.time()
# now = time.strftime("%H:%M", time.localtime(nowStamp))
# print(now)

import time
from selenium import webdriver
driver = webdriver.Chrome()
# driver.maximize_window()
# driver.minimize_window()
# driver.set_window_position(50, 50)
# driver.set_window_size(1920, 900)
driver.get("http://www.naver.com")
print(driver.title)
print(driver.current_url)
time.sleep(5)
