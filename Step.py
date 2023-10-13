def power(a, n):
    res = 1
    if n >= 0:
        for i in range(n):
            res = res * a
        return res
    else:
        for i in range(abs(n)):
            res = res / a
        return res
print(power(a = int(input()), n = int(input())))
