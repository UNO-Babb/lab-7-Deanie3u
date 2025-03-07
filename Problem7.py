#Problem7.py
#Project Euler problem 7

from NumberTests import isPrime

def find_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if isPrime(num):
            count += 1
    return num

if __name__ == "__main__":
    factor = 10001
    result = find_prime(factor)
    print("the prime number is:", result)