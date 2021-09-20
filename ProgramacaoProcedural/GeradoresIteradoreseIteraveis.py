import sys
import time

def gera():
    r = []
    for n in range(100):
        yield n
        time.sleep(0.2)

g = gera()

for v in g:
     print(v)