# 1~10 사이의 정수를 입력받아 해당 구구단 단을 출력하기.

a, b = map(int, input().split(" "))

if a > 10 or b > 10 or a == 0 or b == 0:
    print("1~10 사이의 정수 입력해주세요.")
else:
    print(f"{a} * {b} = {a*b}")
