def is_perfect_square(value):
    for i in range(1, value):
        if(i * i == value):
            return True
    return False



for i in range(1, 100):
    print(f"{i} é um quadrado perfeito? {is_perfect_square(i)}")