from equipamento import Equipamento
from computador import Computador

class TestaEquipamento:
    def __main__():
        equipamento = Equipamento('Monitor', 1000)
        computador = Computador('Notebook Lenovo', 4000, '16GB', 'i7')

        equipamento.exibir()
        computador.exibir()




TestaEquipamento.__main__()