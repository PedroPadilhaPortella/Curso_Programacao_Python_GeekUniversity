def fibonnaci(n):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo}, {ultimo}', end=', ')
    while(n > 2):
        proximo = penultimo + ultimo
        print(f"{proximo}", end=', ')
        penultimo = ultimo
        ultimo = proximo
        n -= 1; 

if __name__ == "__main__":
    fibonnaci(12)