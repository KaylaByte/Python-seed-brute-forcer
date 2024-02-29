import random
import time
import itertools
import multiprocessing as mp

# CHANGE THESE VALUES HERE
seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Sequence of numbers the program will attempt to generate a seed for
lower = 1 # Lowest value random.randint() will generate
upper = 10 # Highest value random.randint() will generate
process_total = mp.cpu_count() # How many processes will be used, limited by cpu core count

def brute_force(process_num):
    global seq, process_total, upper, lower
    start_time = time.perf_counter()

    for seed in itertools.count(process_num, process_total): # Starts at 0, increases by 1 each loop
        breakit = 0 # Used to break the loop once sequence is found
        random.seed(seed)
        for seq_item in seq:
            if random.randint(lower, upper) == seq_item:
                breakit += 1
                continue
            break
        if breakit == len(seq):
            break

    end_time = time.perf_counter()

    print(f"Seed: {seed}")
    print("Total gen time: {0:.2f} seconds.".format(end_time - start_time))
    return True

print("Generating...")

# Deals with the multiprocessing, significantly improves speed
pool = mp.Pool(processes=process_total) 

process_num = []
for x in range(process_total):
    process_num.append(x)

processes = pool.imap_unordered(brute_force, process_num)
pool.close()

for process in processes:
    if process:
        pool.terminate()
        break

pool.join()

# n: seed | avg brute force time on my PC
# 1: 2 | instant
# 2: 2 | instant
# 3: 69 | instant
# 4: 2387 | instant
# 5: 146085 | 0.04 seconds
# 6: 365871 | 0.13 seconds
# 7: 2799290 | 0.78 seconds
# 8: 401991108 | 114.11 seconds
# 9: 1361757416 | 397.33 seconds
# 10: 5234703478 | 1536.62 seconds
# Pi: 33327794158 | 9484.80 seconds
