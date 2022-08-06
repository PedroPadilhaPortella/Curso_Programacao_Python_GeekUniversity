'''
    Testes Unitários

    O teste unitário consiste em verificar o comportamento das menores unidades em sua aplicação. Tecnicamente, isso seria uma classe ou até mesmo um método de classe em línguas orientadas a objetos, e seria um procedimento ou função em línguas processuais e funcionais.

    Para rodar os testes, utilizamos unitttest.main()

    Rodando script em modo Verbose:
    > python atividades.test.py -v

    Methods anf what they check:
        assertEqual(a, b)  => a == b
        assertNotEqual(a, b) => a != b
        assertTrue(x) => bool(x) is True
        assertFalse(x) => bool(x) is False
        assertIs(a, b) => a is b
        assertIsNot(a, b) => a is not b
        assertIsNone(x) => x is None
        assertIsNotNone(x) => x is not None
        assertIn(a, b) => a in b
        assertNotIn(a, b) => a not in b
        assertIsInstance(a, b) => isinstance(a, b)
        assertNotIsInstance(a, b) => not isinstance(a, b)

    Nos testes também podemos usar DocStrings e pré hooks:

    setup() -> Executa antes de cada teste, usado para criar conexões e executar metodos antes do teste.
    tearDown() -> Executa após cada teste, usado para excluir dados ou fechar conexões.
    
'''
from atividades import comer, dormir, is_funny
import unittest

class AtividadesTest(unittest.TestCase):

    def setUp(self) -> None:
        # Configurações para serem executadas antes de cada teste
        return super().setUp()

    def tearDown(self) -> None:
        # Configurações para serem executadas após cada teste
        return super().tearDown()
    
    def test_comer_saudavel(self):
        '''
            Testando retorno de alimentação saudavel
        '''
        self.assertEqual(
            comer('banana', is_saudavel=True),
            'banana é saudável'
        )

    def test_comer_pizza(self):
        '''
            Testando retorno de alimentação não saudavel
        '''
        self.assertEqual(
            comer('pizza', is_saudavel=False),
            'pizza não é saudável'
        )

    def test_dormir_muito(self):
        '''
            Testando resultado de dormir mais de 8 horas
        '''
        self.assertEqual(
            dormir(9),
            'parece que a noite foi longa'
        )

    def test_dormir_pouco(self):
        '''
            Testando resultado de dormir menos de 8 horas
        '''
        self.assertEqual(
            dormir(4),
            'você está dormindo pouco'
        )

    def test_is_funny(self):
        '''
            Testando se a pessoa é engraçada
        '''
        self.assertEqual(is_funny('Danilo Gentili'), True)
        self.assertEqual(is_funny('Bruna Louise'), False)

if __name__ == '__main__':
    unittest.main()