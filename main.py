def main(x):
    k = 0
    for _ in range(3):
        k += x - 1
    return k


a = int(input())
print(main(main(a)) - main(a))
