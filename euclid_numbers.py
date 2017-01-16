#!/usr/bin/python

#########################################
## CS 3430: S2017: HW01: Euclid Numbers
## David Browning
## A01256705
#########################################

import math

def is_prime(n):
    '''is_prime(n) ---> True if n is prime; False otherwise.'''
    if(n <= 1):
        ##('false');
        return False;
    elif(n <= 3):
        ##('true');
        return True;
    elif(n % 2 == 0 or n % 3 == 0):
        ##('false');
        return False;
    i = 5;
    while(i * i <= n):
        if (n%i == 0 | n % (i+2) == 0):
            ##('false');
            return False;
        i = i + 6;
    ##('true');
    return True;
    pass 

##Modeled after the pseudo code found on wikipedia. https://en.wikipedia.org/wiki/Primality_test#Pseudocode

def next_prime_after(p):
    '''computes next prime after prime p; if p is not prime, returns None.'''
    if not is_prime(p): return None
    ## your code here
    p += 1;
    while (not is_prime(p)):
        p += 1;
    return p;
    pass

def euclid_number(i):
    '''euclid_number(i) --> i-th Euclid number.'''
    ##Had epiphany that passing dynamic_typing
    ## to next_primer_after was casing the 'NoneType' return;
    if i < 0: return None
    ## your code here
    eu_num = 1;
    dynamic_typing = 0;
    for num in xrange(i): 
        dynamic_typing = num;
        eu_num = eu_num*next_prime_after(dynamic_typing); # <-- This here. 
    return eu_num;
    pass

def compute_first_n_eucs(n):
    '''returns a list of the first n euclid numbers.'''
    eucs = []
    ## your code here
    for eu_num in xrange(n):
        eucs.append(euclid_number(eu_num));

    return eucs

def prime_factors_of(n):
    '''returns a list of prime factors of n if n > 1 and [] otherwise.'''
    if n < 2: return []
    factors = []
    ## your code here
    return factors

def tabulate_euc_factors(n):
    '''returns a list of 3-tuples (i, euc, factors).'''
    euc_factors = []
    ## your code here
    return euc_factors





                     

    

