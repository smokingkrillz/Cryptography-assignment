import numpy as np
# this finds the greatest common divisor of two numbers
def gcd(a, b):
    if(b == 0):
        return abs(a)
    else:
        return gcd(b, a % b)
#this function is used by pollard rho function
def f(x,i):
    return x**2 +i
#this function checks if the factor already exists 
def factor_exist(x,arr1):
    for i in arr1:
        if(i == x):
            return True
    return False
#this is the function that finds the actual factors
def Pollard_Rho(n,x1):
    if(n==1):
        return n
    x = x1
    x_d = f(x,x1) % n
    p = gcd(x-x_d,n)
    while p == 1:
        x = f(x,x1)% n
        x_d = f(x_d,x1)% n
        x_d = f(x_d,x1)% n
        p = gcd(x-x_d,n)
    if p == n:
        return -1
    else:
        return p
# a pseudoprime number from exercise 1)    
prime_one = 12243909740653143741634051956588002706538922677067945297771090577047070432082882704919529903007358700037889913509678259418955840419746353883211683843696803
prime_one = (prime_one-1) >> 1
list_of_factors_1 = np.array([])
#finds a list of non-trvial factors
for i in range(20000):
    factor = Pollard_Rho(prime_one,i)
    if factor == -1:
        continue
    if  not factor_exist(factor,list_of_factors_1):
        list_of_factors_1 = np.append(factor,list_of_factors_1)

print("first prime factoers",list_of_factors_1)
# a second pseudoprime number from exercise 1)   
prime_two = 8798551983102538467574071934449311792550577445358651758674507503967046126975140358791389002389850831090390845964187600888402999327260105953110208038958889
prime_two = (prime_two-1) >> 1
list_of_factors_2 = np.array([])

for i in range(30000):
    factor = Pollard_Rho(prime_two,i)
    if factor == -1:
        continue
    if  not factor_exist(factor,list_of_factors_2):
        list_of_factors_2 = np.append(factor,list_of_factors_2)

print(list_of_factors_2)
