# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time
wait_time:int = 1
attempt:int =0 
max_retries:int = 5

while attempt < max_retries:
    print(" attemt",attempt+1, " and wait time is :",wait_time,)
    time.sleep(wait_time) 
    wait_time *= 2
    attempt += 1


 

