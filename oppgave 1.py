
import numpy as np
import random as rand
import math as mt
from timeit import default_timer as timer
'''
201,202,208,209
'''
#this function finds a k value and an odd number m such that (2^k)*m == n
#n is the randomly generated 512 bit number
def find_k_and_m(number):
    n = number-1
    it = 0
    m = 0
    for i in range(0,512):
        if(n % 2 != 0):
            m = n
            it = i
            break
        n = n >> 1
    return it,m

#this is the actual Miller Rabin test
def Miller_Rabin_alg(n): 
    (k,m) = find_k_and_m(n)
    a = rand.randint(1,n-1)
    b= pow(a,m,n)
    if b % n == 1:
        return False
    for i in range(k):
        if b % n == n-1:
            return False
        else:
            b= (b**2) % n
    return True

#finds the two numbers and times the time it took to generate it
prime_one=0
prime_two=0
time_r1_start = timer()
while True:
    r_num = rand.randint(2**511,(2**512)-1)
    if r_num % 2 == 0:
        r_num = r_num-1
    if not Miller_Rabin_alg(r_num):
        prime_one = r_num
        time_r1_end = timer()
        break
time_r1 = time_r1_end-time_r1_start
print("time taken for r1 is ",time_r1 )
time_r2_start = timer()

while True:
    r_num = rand.randint(2**511,(2**512)-1)
    if r_num % 2 == 0:
        r_num = r_num-1
    if not Miller_Rabin_alg(r_num) and r_num != prime_one :
        prime_two = r_num
        time_r2_end = timer()
        break
time_r2 = time_r2_end-time_r2_start
print("time taken for r2 is ", time_r2)
print("First prime is", prime_one)
print("Second prime is", prime_two)
