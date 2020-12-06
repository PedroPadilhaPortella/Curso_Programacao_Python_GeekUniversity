x = [1, 9, 6, 8, 11]
y = [2, 7, 9, 3, 6]
sum = []
product = []
diff = []
interssec = set()
union = set()

for i, e in enumerate(x):
    #sum
    sum.append(x[i] + y[i])
    #product
    product.append(x[i] * y[i])
    #diff
    diff.append(x[i] - y[i])
    #interssection
    interssec = set(x).intersection(set(y))
    #union
    union = set(x).union(set(y))

print("Sum {}".format(sum))
print("Product {}".format(product))
print("Difference {}".format(diff))
print("Interssection {}".format(interssec))
print("Union {}".format(union))