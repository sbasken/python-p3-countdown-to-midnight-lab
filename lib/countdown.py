import time# your code goes here!


def countdown(int):
    num = int
    while num > 0:
        print(f"{num} SECOND(S)!")
        num -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(int):
    num = int
    while num > 0:
        print(f"{num} SECOND(S)!")
        num -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")

countdown_with_sleep(10)