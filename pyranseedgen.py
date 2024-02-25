import random
import time

def run():
    seed = 0 # starts at 0, increases by 1 each loop
    goto = 10 # length of brute-forced sequence

    start_time = time.perf_counter()
    print("Generating...")

    seq_len = 1
    while seq_len <= goto:
        random.seed(seed)
        for seq_len in range(1, goto + 2):
            if random.randint(1,10) != seq_len:
                break
        seed += 1

    end_time = time.perf_counter()

    print(f"Seed: {seed - 1}")
    print("Total gen time: {0:.2f} seconds.".format(end_time - start_time))

run()

# n: seed | avg brute force time on my PC
# 1: 2 | instant
# 2: 2 | instant
# 3: 69 | instant
# 4: 2387 | 0.01 seconds
# 5: 146085 | 0.51 seconds
# 6: 365871 | 1.26 seconds
# 7: 2799290 | 9.60 seconds
# 8: 401991108 | 1385.41 seconds (~ 23 minutes) 
# 9: 1361757416 | 4705.57 seconds (~ 1 hour 18 minutes)
# 10: 5234703478 | 18064.07 seconds (~ 5 hours 1 minute)
