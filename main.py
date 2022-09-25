def main(x):
    k = 0
    for _ in range(5):
        k += x - 2
    return k


a = int(input())
print(main(main(a)) - main(a))
