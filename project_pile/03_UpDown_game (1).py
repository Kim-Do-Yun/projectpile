import random
'''
프로그램의 조건은 다음과 같습니다. 다음 조건에 알맞는 Up&Down 게임을 만들어봅시다.

1. 사용자에게 최소값과 최대값을 입력 받습니다. (단, 최소값이 최대값보다 작지 않다면 다시 입력받아야 합니다.)
2. 숨겨진 값은 최소값부터 최대값 사이의 랜덤한 하나로 설정합니다.
3. 추측 방식
    - computer는 항상 최소와 최대값의 평균 값으로 추측합니다.
    - 사용자는 항상 숫자를 입력받습니다.
4. 범위를 점차 좁혀가면서, 범위의 범주를 넘으면 "최소값부터 최대값사이의 값을 넣어야한다"는 메시지를 보여줍니다.
5. 누가 이겼는지, 몇번만에 이겼는지도 같이 보여줍니다.
'''
while True:
    mini_number = int(input("최소값을 입력해주세요 : "))
    max_number = int(input("최대값을 입력해주세요 : "))
    if mini_number <= max_number:
        check_number = random.randint(mini_number,max_number)
        break
    else:
        print("다시 입력해주세요.")
        continue

i = 0
mini = mini_number
maxx = max_number
while True:
    dab = int(input("답: "))
    computer = (mini + maxx) / 2
    i += 1
    mini += 1
    maxx -= 1
    if dab < mini_number or dab > max_number:
        print("최소값부터 최대값사이의 값을 넣어야 한다.")
        i += 1
    elif check_number > dab:
        print("정답은 답보다 더 큽니다.")
        i += 1
    elif dab > check_number:
        print("정답은 답보다 더 작습니다.")
        i += 1
    if dab != check_number and computer == check_number:
        print("컴퓨터가",i,"번만에 이겼습니다.")
        break
    elif computer != check_number and dab == check_number:
        print("플레이어가",i,"번만에 이겼습니다.")
        break


'''
while mini_number >= max_number:
    print("다시 입력해주십시오.")
    mini_number = int(input("최소값을 입력해주세요 : "))
    max_number = int(input("최대값을 입력해주세요 : "))
else:
    check_number = random.randint(mini_number,max_number)
 
i = 1
while mini_number < check_number < max_number:
    dab = int(input("답: "))
    computer = ((mini_number+max_number)/2)
    if (dab == check_number or computer == check_number):
        print(i,"번만에 이겼습니다.")

        break
    elif (mini_number >= dab):
        print("최소값보다 작습니다.")
        i += 1
    elif dab >= max_number:
        print("최대값보다 큽니다.")
        i += 1
    elif mini_number <= dab < check_number:
        print("정답보다 작습니다.")
        mini_number = dab
        i += 1
        j += 1
    elif check_number <= dab < max_number:
        print("정답보다 큽니다.")
        max_number = dab
        i += 1
        j += 1
    elif dab == check_number and computer == check_number:
        print(i,"번만에 무승부입니다.")
        break
'''