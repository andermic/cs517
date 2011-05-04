#! /usr/bin/python

import matplotlib.pyplot as plot

lines = open('results.txt', 'r').readlines()
lines = [i.strip().split(',') for i in lines if i != '\n']

probs = {}
times = {}
for line in lines:
    if probs.get(int(line[0])) == None:
        probs[int(line[0])] = []
        times[int(line[0])] = []
    probs[int(line[0])].append([float(line[1]),float(line[2])])
    times[int(line[0])].append([float(line[1]),float(line[3])])

n = 1000
xs = [i[0] for i in times[n]]
ys = [i[1] for i in times[n]]

plot.title(r'Runtime as a function of density, $n$ = %d' % n)
plot.xlabel('$Density$')
plot.ylabel('$Runtime$')
plot.plot(xs,ys)
plot.show()

