'''
    Try - Except - Else - Finally

    O bloco try é executado primeiro, e se ocorrer algum erro, o bloco except é executado.
    O bloco finally é executado independente se ocorrer ou não um erro.

    try:
        # Executa o bloco de código
    except:
        # Executa o bloco de código caso ocorra um erro
    else:
        # Executa o bloco de código caso não ocorra um erro
    finally:
        # Executa o bloco de código independente se ocorrer ou não um erro

    Exemplo:
    Toda entrada do usuário deve ser tratada em um try, caso ocorra algum erro.

'''

try:
    print(5/0)
except ArithmeticError as err:
    print('Não podemos dividir por zero: ')
    print(err)
except:
    print('Ocorreu um erro')
else:
    print('Não ocorreu erro')
finally:
    print('Finalizando execução')

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        print(f'Ocorreu um problema:: {err}')


num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')

dividir(num1, num2)