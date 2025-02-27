import time
import math

num = int(input())
milliseconds = int(input())

time.sleep(milliseconds / 1000)
result = math.sqrt(num)
print(f"Square root of {num} after {milliseconds} milliseconds is {result}")
