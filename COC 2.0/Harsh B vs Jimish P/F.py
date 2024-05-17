n = int(input())
def prime_factors(num):
    factors = []
    divisor = 2
    while divisor * divisor <= num:
        while (num % divisor) == 0:
            factors.append(divisor)
            num //= divisor
        divisor += 1
    if num > 1:
        factors.append(num)
    return set(factors)
prime = prime_factors(n)
ans = 1
for p in prime:
    ans *= p
print(ans)