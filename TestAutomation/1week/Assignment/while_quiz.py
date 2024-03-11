# while 문을 이용해 사용자에게 'exit'를 입력받기 전까지 계속 입력받기.

user_answer = input()

while True:
    if user_answer == 'exit':
        break
    user_answer = input()
