x = [0, 1, 2, 3, 4, 5]
y = [0, 0, 0, 0, 0, 0]
k = 0
for k in x:
    z = 2 * k + 1
    y[k] = z
    k = k + 1

print("x = " + str(x))
print("y = " + str(y))
