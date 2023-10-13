def bank(a, years):

    for i in range(years):
        a += a / 10
    print(a)

bank(int(input()),int(input()))


