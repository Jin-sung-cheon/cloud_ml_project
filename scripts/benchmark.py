import time
from app.utils import optimize_tokens
from app.model import predict

TEXT = "Hello!!!! THIS IS   A CRAZZY   SAMPLE TEXT 12345 !!!"

# raw
t0 = time.time()
predict(TEXT)
raw_time = time.time() - t0

# optimized
opt = optimize_tokens(TEXT)
t1 = time.time()
predict(opt)
opt_time = time.time() - t1

print("Raw input time:", raw_time)
print("Optimized input time:", opt_time)
print("Speedup:", raw_time / opt_time)
