import math

def sum_from_sieve_of_eratosthenes(n):

    is_prime = [True]*(n+1)
    is_prime[0] = False
    is_prime[1] = False
    
    for i in range (2, int(math.sqrt(n)) + 1) :
        if is_prime[i]==True :
            for j in range(i*i, n+1, i) :
                is_prime[j]= False

    sum = 0
    for i in range(n+1):
        if is_prime[i]:
           sum += i 
    return sum



n = input("Enter a positive number: ")
n = int(n)

if (n<=0) :
    raise ValueError("Enter a positive number")

sum = sum_from_sieve_of_eratosthenes(n)
print("Sum : ", sum, "\n")
