import random
import time

seed = 0 # starts at 0, increases by 1 each loop
breakit = 0 # amount of numbers that have worked successfully
goto = 10 # length of brute-forced sequence

start_time = time.perf_counter()
print("Generating...")

while breakit < goto:
    random.seed(seed)
    for x in range(1, goto + 1, 1):
        if random.randint(1,10) == x:
            breakit += 1
        else:
            seed += 1
            breakit = 0
            break

end_time = time.perf_counter()

print(f"Seed: {seed - 1}")
print("Total gen time: {0:.2f} seconds.".format(end_time - start_time))

# n: seed | avg brute force time on my PC
# 1: 2 | instant
# 2: 2 | instant
# 3: 69 | instant
# 4: 2387 | 0.01 seconds
# 5: 146085 | 0.52 seconds
# 6: 365871 | 1.30 seconds
# 7: 2799290 | 9.91 seconds
# 8: 401991108 | time unknown
# 9: 1361757416 | time unknown
# 10: 5234703478 | ~ 5 hours 12 minutes (whilst doing additional checks, so likely inaccurate)
