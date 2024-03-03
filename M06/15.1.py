# 15.1

import multiprocessing
import random
import time
from datetime import datetime

def process_function():
    wait_time = random.random()  # Generate a random wait time between 0 and 1
    time.sleep(wait_time)  # Sleep for the random wait time
    current_time = datetime.now().strftime("%H:%M:%S")  # Get current time
    print(f"Current time: {current_time}")
    print("Exiting process.")

if __name__ == "__main__":
    processes = []
    for _ in range(3):
        p = multiprocessing.Process(target=process_function)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()  # Wait for all processes to finish
