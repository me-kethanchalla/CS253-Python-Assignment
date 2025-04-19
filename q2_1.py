import math

def sum_from_sieve_of_eratosthenes(n):

    # For small n
    # we are just using something enough to cover the first 5 primes
    if n < 6:
        bound = 15
    else:
        #  n*(ln(n) + ln( ln( n))) for long n's
        bound = int(n * (math.log(n) + math.log(math.log(n)))) + 1

    # we are using upto bound only
    is_prime = [True] * (bound + 1) 

    is_prime[0:2] = [False, False]
    limit = int(math.isqrt(bound))

    for i in range(2, limit + 1):
        if is_prime[i]:
            for multiple in range(i*i, bound + 1, i):
                is_prime[multiple] = False

    total = 0
    count = 0
    for i in range(2, bound + 1):
        if is_prime[i]:
            total += i
            count += 1
            if count == n:
                break

    # Just in case the bound was too small (extremely unlikely for reasonable n)
    if count < n:
        raise RuntimeError(f"Prime bound {bound} too low for n={n}")

    return total




n = input("Enter a positive number: ")

n = int(n)

if (n<=0) :
    raise ValueError("Enter a positive number")

sum = sum_from_sieve_of_eratosthenes(n)
print("Sum : ", sum, "\n")
