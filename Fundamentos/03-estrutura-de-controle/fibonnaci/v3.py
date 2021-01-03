def fibonnaci(n):
    resultado = [0, 1]
    while(len(resultado) < n):
        resultado.append(resultado[-2] + resultado[-1])
    return resultado

if __name__ == "__main__":
    resultado = fibonnaci(12)
    print(resultado)