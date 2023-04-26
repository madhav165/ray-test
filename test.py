import ray
import time
import math

@ray.remote
def double(x):
    return x* 2

s = time.time()
res = [double(i) for i in range(10000)]
e = time.time()
print(e-s) #0.005931854248046875

ray.init()

s = time.time()
res_ref = [double.remote(i) for i in range(10000)]
res = ray.get(res_ref)
e = time.time()
print(e-s) #3.1759698390960693

ray.shutdown()