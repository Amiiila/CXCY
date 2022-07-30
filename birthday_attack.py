from gmssl import sm3,func
from time import time
import random


start=time()
while True:
    m1=bytes(str(random.randint(0,2**16)), encoding='utf-8')
    h1 = sm3.sm3_hash(func.bytes_to_list(m1))
    m2=bytes(str(random.randint(0,2**16)), encoding='utf-8')
    h2 = sm3.sm3_hash(func.bytes_to_list(m2))
    if h1 == h2:
        print(h1)
        break
print("Time:",time()-start)
