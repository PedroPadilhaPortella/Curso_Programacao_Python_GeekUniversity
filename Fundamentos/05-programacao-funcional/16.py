def desenha_linha(quantidade = 1):
    string = ''
    for i in range(0, quantidade):
        string += '='
    return string


print(desenha_linha(3))
print(desenha_linha(100))
print(desenha_linha())