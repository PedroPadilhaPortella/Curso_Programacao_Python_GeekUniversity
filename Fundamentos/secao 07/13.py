vector = []
for i in range(0, 5):
    vector.append(float(input(f"Valor {i}: ")))
print(vector)
print("Posição do maior: {}\nPosição do menor: {}".format(vector.index(max(vector)), vector.index(min(vector))))