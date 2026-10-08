even = range(0, 101, 5)
print(list(even))
even2 = []
for i in even:
    if i % 6 == 0:
        even2.append(i)
print(list(even2))