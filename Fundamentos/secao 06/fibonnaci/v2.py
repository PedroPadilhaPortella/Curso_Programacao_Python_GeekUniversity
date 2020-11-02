def fibonnaci(n):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo}', end=', ')
    while(n > 1):
        print(f"{ultimo}", end=', ')
        penultimo, ultimo = ultimo, penultimo + ultimo
        n -= 1

if __name__ == "__main__":
    fibonnaci(12)