while True:
    s = input("Введіть речення: ")
    if len(s)>= 3:
        break

third = s[2::3]
print(third, " ")