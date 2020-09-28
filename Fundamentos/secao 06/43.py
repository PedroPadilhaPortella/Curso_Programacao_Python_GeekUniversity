total = 0
people = 0
while(True):
    age = int(input("Sua idade: "))
    if(age <= 0):
        break
    total += age
    people += 1
media = total / people
print(f"Media das {people} idades = {media}")