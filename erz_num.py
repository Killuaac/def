def is_prime(num):
    f = True
    for i in range(2,int(num ** 0.5)):
        if num % i == 0:
            f = False
    return f
num = int(input())
print(is_prime(num))
