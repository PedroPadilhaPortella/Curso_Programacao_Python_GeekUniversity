array = []
for i in range(1, 6):
    array.append(float(input(f"Valor {i}: ")))

print(array)
media = sum(array) / len(array)
print("Maior: {}, menor: {}, media: {:.2f}".format(max(array), min(array), media))