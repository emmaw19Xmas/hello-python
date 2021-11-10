import random
target_Number = random.randint(1, 100)


while True:
    people_Number = int(input("请输入一个整数："))
    if people_Number > target_Number:
        print("太大了，请重试")
    elif people_Number < target_Number:
        print("太小了，请重试")
    else:
        print("恭喜你，猜对啦！")
        break