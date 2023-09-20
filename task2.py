while True:
    n = input("Введіть значення n(6 символів): ")
    if len(n) == 6:
        if n.isdigit():
            break

sum = 0
for symbol in n:
    number = int(symbol)
    sum+=number

print(sum)