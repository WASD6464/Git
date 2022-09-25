def main(x):
    k = 0
    c = 0
    for _ in range(5):
        k += x + 2
        c = k / 2
    return k + c


a = int(input())
print(main(a))

def x_in_cube(n):
    return n**3
