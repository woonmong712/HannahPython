# 1. Selenium과 Python을 이용해 임의의 페이지 5개에 접근하기.
# 2. 접근한 페이지들의 타이틀을 title = [] 리스트에 추가하기.
# 3. 접근한 페이지들의 URL을 url = [] 리스트에 추가하기.

import time
from selenium import webdriver

driver = webdriver.Chrome()
title, url = [], []

driver.get("https://www.google.com")
title.append(driver.title)
url.append(driver.current_url)

driver.get("https://www.naver.com")
title.append(driver.title)
url.append(driver.current_url)

driver.get("https://www.daum.net/")
title.append(driver.title)
url.append(driver.current_url)

driver.get("https://www.youtube.com/")
title.append(driver.title)
url.append(driver.current_url)

driver.get("https://www.op.gg/")
title.append(driver.title)
url.append(driver.current_url)

# 4. title 리스트와 url 리스트를 출력하기.
print(f"TITLE : {title}\nURL : {url}")
