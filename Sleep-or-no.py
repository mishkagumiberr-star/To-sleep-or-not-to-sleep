import random
import time
sleep = random.randint(1, 2)
print(f"sleep: {sleep}")
print("""1 = go sleep""")
print("""2 = dont go sleep""")
print("")
while True:
    if sleep == 1:
        print("well, go sleep pls")
        time.sleep(6)
        break
    elif sleep == 2:
        print("well... dont sleep lol")
        time.sleep(6)
        break