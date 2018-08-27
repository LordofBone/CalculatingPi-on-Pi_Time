import os
import time

start = time.time()
os.system('echo "scale=5000; 4*a(1)" | bc -l')
end = time.time()
print("\nTime Taken: " + str(end - start))