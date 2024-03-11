#1. 3주차 과제로 제출한 테스트에 예외처리 하기.
#2. 3주차 과제로 제출한 내용의 테스트 결과 리포트를 txt 파일로 만들 수 있도록 구현하기.
#- 결과 리포트의 구성은 직접 구성해 보세요!

import time
import requests
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# 현재 시간 구하기
now = time.strftime('%Y_%m_%d_%Hh_%Mm')
result_pass_list = [] # 성공한 케이스가 담기는 곳
result_fail_list = [] # 실패한 케이스가 담기는 곳
fail_reason_list = [] #실패한 이유가 담기는 곳
tc_count = 0 # TC count

#  테스트 결과가 담길 폴더 생성
if not os.path.exists('test_result'):
    os.makedirs('test_result')

f = open(f'./test_result/{now}_test_report.txt','w')


# 전체 테스트 케이스에 대한 예외처리
try:
    # TC_01. 홈페이지 접속
    try:
        tc_id = 'TC_001'
        tc_count += 1
        if (driver.current_url == "https://www.aladin.co.kr/home/welcome.aspx"):
            print(f'홈페이지 접속 성공\n{tc_id} : PASS')
            result_pass_list.append(tc_id)
        else:
            print(f'홈페이지 접속 실패\n{tc_id} : FAIL')
            print(driver.current_url)
            result_fail_list.append(tc_id)
            fail_reason_list.append(f'홈페이지 접속 실패 : {driver.current_url}\n')
    except Exception as e:
        print(f"{tc_id} 수행 실패 >>> {e}")

    driver.implicitly_wait(10)

    # TC_02. 비유효한 도서명 검색
    try:
        tc_id = 'TC_002'
        tc_count += 1
        book_title_01 = 'ㅁㄴㅇ런이ㅏ러 ㅁ'
        search_box = driver.find_element(By.CSS_SELECTOR,'#SearchWord')
        search_box.click()
        search_box.send_keys(book_title_01)
        driver.find_element(By.CLASS_NAME,'search_btn').click()

        check_text = f"'{book_title_01}'에 대한 검색 결과가 없습니다."
        search_result_01 = driver.find_element(By.CSS_SELECTOR,'#wa_SearchResult_wa_search3_Result1_wa_search3_Result_NoResult1_panDefault > div > div.ss_line > table > tbody > tr > td > div')
        if (check_text == search_result_01.text):
            print(f'비유효한 도서명 검색 성공\n{tc_id} : PASS')
            result_pass_list.append(tc_id)
        else:
            print(f'비유효한 도서명 검색 실패\n{tc_id}: FAIL')
            print(search_result_01)
            result_fail_list.append(tc_id)
            fail_reason_list.append(f'비유효한 도서명 검색 실패 : {search_result_01}\n')
    except Exception as e:
        print(f"{tc_id} 수행 실패 >>> {e}")

    time.sleep(3)

    # TC_03. 유효한 도서명 검색 (한글)
    try:
        tc_id = 'TC_003'
        tc_count += 1
        book_title_02 = '오래 준비해온 대답'
        search_box = driver.find_element(By.CSS_SELECTOR,'#SearchWord')
        search_box.click()
        search_box.clear()
        search_box.send_keys(book_title_02)
        driver.find_element(By.CLASS_NAME,'search_btn').click()

        search_result_02 = driver.find_element(By.CSS_SELECTOR,'#Search3_Result > div:nth-child(1) > table > tbody > tr > td:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > ul > li:nth-child(1) > a.bo3')
        if (book_title_02 == search_result_02.text):
            print(f'유효한 도서명(한글) 검색 성공\n{tc_id}: PASS')
            result_pass_list.append(tc_id)
        else:
            print(f'유효한 도서(한글) 검색 실패\n{tc_id} : Fail')
            print(search_result_02.text)
            result_fail_list.append(tc_id)
            fail_reason_list.append(f'유효한 도서(한글) 검색 실패 : {search_result_02.text}\n')
    except Exception as e:
        print(f"{tc_id} 수행 실패 >>> {e}")

    time.sleep(3)

    # TC_04. 유효한 도서명 검색 (영어)
    try:
        tc_id = 'TC_004'
        tc_count += 1
        book_title_03 = 'The Little Prince'
        search_box = driver.find_element(By.CSS_SELECTOR,'#SearchWord')
        search_box.click()
        search_box.clear()
        search_box.send_keys(book_title_03)
        driver.find_element(By.CLASS_NAME,'search_btn').click()

        search_result_03 = driver.find_element(By.CSS_SELECTOR,'#Search3_Result > div:nth-child(1) > table > tbody > tr > td:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > ul > li:nth-child(2) > a')
        if (book_title_03 == search_result_03.text):
            print(f'유효한 도서명(영어) 검색 성공\n{tc_id} : PASS')
            result_pass_list.append(tc_id)
        elif book_title_03 in search_result_03.text:
            print(f'유효한 도서명(영어) 검색 성공\n{tc_id} : PASS')
            result_pass_list.append(tc_id)
            print(search_result_03.text)
        else:
            print(f'유효한 도서(영어) 검색 실패\n{tc_id} : Fail')
            print(search_result_03.text)
            result_fail_list.append(tc_id)
            fail_reason_list.append(f'유효한 도서(영어) 검색 실패 : {search_result_03.text}\n')
    except Exception as e:
        print(f"{tc_id} 수행 실패 >>> {e}")

    time.sleep(3)
    
    # TC_05. 특수문자 포함 음반 검색
    try:
        tc_id = 'TC_005'
        tc_count += 1
        music_title_01 = '[미니 CD]'
        search_box = driver.find_element(By.CSS_SELECTOR,'#SearchWord')
        search_box.click()
        search_box.clear()
        search_box.send_keys(music_title_01)
        driver.find_element(By.CLASS_NAME,'search_btn').click()

        search_result_04 = driver.find_element(By.CSS_SELECTOR,'#Search3_Result > div:nth-child(1) > table > tbody > tr > td:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > ul > li:nth-child(1) > a.bo3')
        if (music_title_01 == search_result_04.text):
            print(f'특수문자 포함된 음반명 검색 성공\n{tc_id} : PASS')
            result_pass_list.append(tc_id)
        elif music_title_01 in search_result_04.text:
            print(f'특수문자 포함된 음반명 검색 성공\n{tc_id} : PASS')
            result_pass_list.append(tc_id)
            print(search_result_04.text)
        else:
            print(f'특수문자 포함된 음반명 검색 실패\n{tc_id} : Fail')
            print(search_result_04.text)
            result_fail_list.append(tc_id)
            fail_reason_list.append(f'특수문자 포함된 음반명 검색 실패 : {search_result_04.text}\n')
    except Exception as e:
        print(f"{tc_id} 수행 실패 >>> {e}")

    time.sleep(3)

    # TC_06. 검색한 음반 클릭하여 상세 페이지 접속
    try:
        tc_id = 'TC_006'
        tc_count += 1
        driver.find_element(By.CSS_SELECTOR,'#Search3_Result > div:nth-child(1) > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(1) > td > div > a > img').click()
        result_text = driver.find_element(By.CSS_SELECTOR,'#Ere_prod_allwrap > div.Ere_prod_bookwrap > div.Ere_prod_Binfowrap > div > div:nth-child(1) > ul > li:nth-child(1) > div.Litem')
        check_text = '판매가'

        if (check_text == result_text.text):
            print(f'상세 페이지 접속 성공\n{tc_id} : PASS')
            result_pass_list.append(tc_id)
        else:
            print(f'상세 페이지 접속 실패\n{tc_id} : Fail')
            print(result_text.text)
            result_fail_list.append(tc_id)
            fail_reason_list.append(f'상세 페이지 접속 실패 : {result_text.text}\n')
    except Exception as e:
        print(f"{tc_id} 수행 실패 >>> {e}")

    # TC_07. 알라딘 로고 버튼 기능 확인
    try:
        tc_id = 'TC_007'
        tc_count += 1
        driver.find_element(By.CSS_SELECTOR,'#logoBtn > img').click()
        if (driver.current_url == "https://www.aladin.co.kr/home/welcome.aspx"):
            print(f'홈페이지 접속 성공\n{tc_id}: PASS')
            result_pass_list.append(tc_id)
        else:
            print(f'홈페이지 접속 실패\n{tc_id} : FAIL')
            print(driver.current_url)
            result_fail_list.append(tc_id)
            fail_reason_list.append('f홈페이지 접속 실패 : {driver.current_url}\n')
    except Exception as e:
        print(f"{tc_id} 수행 실패 >>> {e}")
    
    # TC_08. 위치 이동
    try:
        tc_id = 'TC_008'
        tc_count += 1
        driver.execute_script("window.scrollTo(0,500)")
        print(f"{tc_id} 수행 성공\nTC_08 : PASS")
        result_pass_list.append(tc_id)
        time.sleep(3)
    except Exception as e:
        print(f"{tc_id} 수행 실패 >>> {e}")

    # TC_09. 실패한 케이스 확인하기
    try:
        tc_id = 'TC_009'
        tc_count += 1
        url = 'https://woonmong712.github.io/portfolioSJ/'
        response = requests.get(url)
        status_code = response.status_code
        if status_code == 200:
            print(f'홈페이지 접속 성공\n{tc_id} : PASS')
            result_pass_list.append(tc_id)
        else:
            print(f'홈페이지 오류 발생\n{tc_id} : FAIL')
            result_fail_list.append(tc_id)
            fail_reason_list.append(f'홈페이지 오류 발생 : {status_code}\n')
    except Exception as e:
        print(f"{tc_id} 수행 실패 >>> {e}")


except Exception as e:
    print(f"전체 테스트 케이스 수행 실패 >>> {e}")




# 통계
f.write(f"테스트 수행 일자 : {now}")
f.write(f'\n[RESULT - PASS]\n')

for pass_cnt in range(len(result_pass_list)):
    f.write(f'{result_pass_list[pass_cnt]}\n')

f.write(f'\n[RESULT - FAIL]\n')
for fail_cnt in range(len(result_fail_list)):
    f.write(f'{result_fail_list[fail_cnt]}\n')
    f.write(f'\t{fail_reason_list[fail_cnt]}\n')

f.write('\n\n=======================\n')
f.write(f'PASS TC COUNT : {len(result_pass_list)}\n')
f.write(f'FAIL TC COUNT : {len(result_fail_list)}\n')
f.write(f'COMPLETED TEST COUNT : {len(result_pass_list)+len(result_fail_list)}\n')
f.write(f'PROGRESS OF TEST : {(len(result_pass_list)+len(result_fail_list))/tc_count*100}%\n')
f.write(f'PASS RATE : {len(result_pass_list)/tc_count*100}%\n')
f.close()
