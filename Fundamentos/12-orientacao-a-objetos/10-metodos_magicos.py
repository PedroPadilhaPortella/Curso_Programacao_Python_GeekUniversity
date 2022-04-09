'''
    Metodos Mágicos
    __init__
    __repr__
    __str__
    __len__
    __del__


'''

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return f'Livro({self.titulo}, {self.autor}, {self.paginas})'

    def __str__(self):
        return f'{self.titulo} escrito por {self.autor}'

    def __len__(self):
        return self.paginas

    def __del__(self):
        print(f'O livro {self.titulo} foi deletado')


livro1 = Livro('Python Rocks', 'Jose', 200)
livro2 = Livro('Java Rocks', 'Maria', 300)

print(livro1)
print(len(livro1))