

def prime_fact(n):
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i = i + 1

    return n


num = 20
print(prime_fact(num))
