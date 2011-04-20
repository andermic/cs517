#! /usr/bin/python

import matplotlib.pyplot as plot

def collatz(num, show_output=False):
    sequence = []
    while num > 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        sequence.append(num)
        if show_output:
            print num,
    if show_output:
        print '\nLength of sequence: %d' % len(sequence)
    return sequence

print '1 - Print the collatz sequence of a given number n'
print '2 - Plot the length of the collatz sequence of all numbers up to n'

choice = input('Choose an option[1,2]: ')
n = input('n: ')

if choice == 1:
    collatz(n, True)
elif choice == 2:
    col_list = []
    for i in range(1, n + 1):
        col_list.append(len(collatz(i)))

    xs = range(1, n + 1)
    ys = col_list

    plot.title(r'Length of Collatz sequence for $x \in [1,%d], x \in \mathbb{N}$' % n)
    plot.xlabel('$x$')
    plot.ylabel('Length of sequence')
    plot.plot(xs,ys)
    plot.show()
