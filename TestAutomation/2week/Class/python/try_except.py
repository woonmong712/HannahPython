# 리스트 크기보다 더 큰 인덱스로 요소에 접근하기
a = [1, 2, 3]
try:
    print(a[4])
except Exception as e:
    print(f"An error occurred!! : {e}")

# 숫자와 문자열 합치기
try:
    result = 3 + 'd'
    print(f"{result}")
except Exception as e:
    print(f"An error occurred!! : {e}")
