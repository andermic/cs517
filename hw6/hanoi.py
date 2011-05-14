#! /usr/bin/python
from math import log

def move_print(A, C):
    print 'Move disk on top of %s to %s' % (A,C)
    temp = conf[ord(A)-65][0]
    conf[ord(A)-65] = conf[ord(A)-65][1:]
    conf[ord(C)-65] = [temp] + conf[ord(C)-65]
    print ' '.join([''.join([{True:'1', False:'0'}[j in i] for j in range(1,d_num+1)]) for i in conf]) + ' -',
    print ' '.join([str(sum([2**(d_num-j) for j in i])) for i in conf]) + '\n'

# Recursive solution
def hanoi(A, B, C, n):
    if n == 1:
        move_print(A, C)
    else:
        hanoi(A, C, B, n - 1)
        move_print(A, C)       
        hanoi(B, A, C, n - 1)

d_num = input("Enter number of disks: ")
print
print '1' * d_num + ' ' + '0' * d_num + ' ' + '0' * d_num + ' - ' + str(2**d_num-1) + ' 0 0'
print
conf = [range(1, d_num + 1),[],[]]
hanoi('A', 'B', 'C', d_num)
