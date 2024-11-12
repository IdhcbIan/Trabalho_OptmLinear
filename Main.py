z = [-1, -2, 1, -4, -5]

print("Antiga")
print(any(x < 0 for x in z[:-1]))
print(any(x > 0 for x in z[:-1]))

found = False
for x in z[:-1]:
    if x > 0:
        found = True
        break

print("Nova")
print(found)





