data = [(1, 1.60), (2, 1.56), (3, 1.76), (4, 1.66), (5, 1.53), (6, 1.90), (7, 1.92), (8, 1.55), (9, 1.78), (10, 1.73)]
maior = data[0][1]
menor = data[0][1]
for d in data:
    if(d[1] > maior):
        maior = d[1]
    if(d[1] < menor):
        menor = d[1]
    
print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"[Id, Altura]: {data}")