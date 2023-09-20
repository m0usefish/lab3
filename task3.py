n = input("Введіть речення: ")
words = n.split()
same=[]
for word in words:
    if word in same:
        res = word
        break
    same.append(word)

print("Слово, що повторюється:", res)