#! /usr/bin/python

from math import ceil
from math import floor
from math import log
from random import choice

# Implementation of Davis-Putnam algorithm
def dp(e, step_num, show_output = False):
    # Treat e as a list of lists, where each list in e is a clause. Denote
    #  the complement of a variable x within a clause as ~x

    if show_output:
        print 'Recursion %d: %s' % (step_num, str(e))
    step_num += 1

    if e == []:
        return True
    for clause in e:
        if clause == []:
            return False
    for i in range(len(e)):
        if len(e[i]) == 1:
            unit_var = e[i][0]
            mod_e = [i for i in e if unit_var not in i]
            if unit_var[0] == '~':
                mod_e = [[j for j in i if j != unit_var[1:]] for i in mod_e]
            else:
                mod_e = [[j for j in i if j != '~' + unit_var] for i in mod_e]
            return dp(mod_e,step_num)
    rand_var = e[0][0]
    if rand_var[0] == '~':
        rand_var = rand_var[1:]
    et = [i for i in e if rand_var not in i]
    et = [[j for j in i if j != '~' + rand_var] for i in et]
    if dp(et,step_num):
        return True
    else:
        rand_var = '~' + rand_var
        ef = [i for i in e if rand_var not in i]
        ef = [[j for j in i if j != rand_var[1:]] for i in ef]
        return dp(ef,step_num)

# A generator for variables names.
def var_gen(input_):
    alphabet = [chr(i+97) for i in range(26)] + \
               [chr(i+65) for i in range(26)]
    power = input_ / 52 + 1
    char = input_ % 52
    return alphabet[char] * power

# Create a random 3-SAT instance with a given number of variables, n; and the
#  ratio of number of clauses to n, density.
def rand_e(n,density):
    variables = [var_gen(i) for i in range(n)]
    num_clauses = int(ceil(n * density))
    e = []
    for i in range(num_clauses):
        clause = []
        for j in range(3):
            while True:
                rand_var = choice(['~','']) + choice(variables)
                if rand_var not in clause:
                    clause.append(rand_var)
                    break
        e.append(clause)
    return e
