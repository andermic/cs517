#! /usr/bin/python

from os import system

# Read a transition function from a user-defined file
file_name = raw_input('Enter a file name containing a transition function: ')
lines = open(file_name, 'r').readlines()
lines = [line for line in lines if line[0] not in ['#','\n',' ']]

# Make a lookup table for pairs of states and symbols
rules = {}
for line in lines:
    line = line.split(' ')
    if rules.get(line[0]) == None:
        rules[line[0]] = {}
    rules[line[0]][line[1]] = [line[3], line[4], line[5].strip()]

# Initialize tape
tape = ['_' for i in range(35)]
input_ = raw_input('Initial input on the tape: ')
for i in range(len(input_)):
    tape[i+1] = input_[i]

choice = ''
head = 1
state = '0'
# Start the simulation
while choice != 'R':
    # Show the tape, current state, and all rules'
    system('clear')
    print ' ' * (head * 2) + '*'
    print ' '.join([tape[i] for i in range(len(tape))])
    print
    print 'Current state: ' + state
    print
    print 'Rules:'
    #print ''.join(lines)

    if state == 'HALT':
        break

    choice = raw_input('[R]un to end, or [Enter] to step: ')
    rule = rules[state][tape[head]]
    state = rule[0]
    tape[head] = rule[1]
    head += {'R':1, 'S':0, 'L':-1}[rule[2]]
    if head < 0 or head > len(tape):
        print 'Head just moved off the tape'
        exit()
