#James Moore
#SDEV 220-50P
#Module 6 Programming Assignment -Concurrency in Python

import datetime
import time
import multiprocessing
import random

# 13.1 Write the current date as a string to the text file today.txt
current_date = datetime.date.today().isoformat()
with open('today.txt', 'w') as f:
    f.write(current_date)

# 13.2 Read the text file today.txt into the string today_string
with open('today.txt', 'r') as f:
    today_string = f.read()

# 13.3 Parse the date from today_string
parsed_date = datetime.datetime.strptime(today_string, '%Y-%m-%d').date()

# 15.1 Multiprocessing to create three separate processes
def worker():
    # Wait a random number of seconds between zero and one
    wait_time = random.random()
    time.sleep(wait_time)
    # Print the current time and exit
    print(f"Process {multiprocessing.current_process().name} - Time: {datetime.datetime.now().strftime('%H:%M:%S')}")

if __name__ == "__main__":
    processes = []
    for i in range(3):
        p = multiprocessing.Process(target=worker)
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
