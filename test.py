stat = 50
k = 1
while stat != 0:
    k += 1
    stat -= 10
print(k)
number = int(input())
user = input()
for _ in range(number - 1):
    print(f'bye, {user}',end="\n")

last_name = input("what is your last name?: ")
print(f"bye, {last_name}")