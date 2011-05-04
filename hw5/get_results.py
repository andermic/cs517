#! /usr/bin/python

from time import time
import matplotlib.pyplot as plot
from davis_putnam import *

n = 200
density = 2.5
num_trials = 100

times = []
satis = 0
unsatis = 0 
for i in range(num_trials):
    start = time()
    result = dp(rand_e(n,density),0)
    elapsed = time() - start
    
    print result, elapsed
    if result:
        satis += 1
    else:
        unsatis += 1
    times.append(elapsed)

print
print 'n: %d, density: %d, num_trials: %d' % (n, density, num_trials)
print 'Prob of satisfiability: %f%%' % (satis/float(num_trials)*100)
print 'Avg time: %f' % (sum(times)/float(num_trials))
