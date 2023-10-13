def distace(x1 = 0, y1 = 0, x2 = 0, y2 = 0):
    dst = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return dst

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

res = distace(x1 = x1, y1 = y1, x2 = x2, y2 = y2)
print(res)
