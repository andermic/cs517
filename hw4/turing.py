#! /usr/bin/python


# Read a transition function from a user-defined file
file_name = raw_input('Enter a file name containing a transition function: ')
trans_func = open(file_name, 'r').readlines()

# Initialize tape
tape = ['_' for i in range(35)]
input_ = raw_input('Initial input on the tape: ')
for i in range(len(input_)):
    tape[i] = input[i]

run_to_end = False
while not run_to_end:
    print ' '.join([tape[i] for i in range(len(tape))])
    
