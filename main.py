print("My program")
def prog(x):
    k = 1
    c = 1
    for _ in range(2):
        k += x -1
        c = k / 3
    return (k + c) * 2


count = int(input())
print(prog(count))

def x_in_square(n):
    return n**2
