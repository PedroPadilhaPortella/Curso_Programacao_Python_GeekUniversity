def sit(a):
    if a < 5.0:
        return 'REPROVADO'
    elif a < 7.0:
        return 'RECUPERAÇÃO'
    else:
        return 'APROVADO'

def gerarGabarito():
    print("--Respostas do Gabarito Oficial--\n")
    gabarito = [input(f"Questão {x + 1}:") for x in range(10)]
    return gabarito

def salvarNotasDosAlunos(gabarito):
    aluno = {}
    turma = []
    print("\n---Gabarito dos Alunos---\n")
    for i in range(3):
        aluno['nome'] = input(f'Nome do aluno {i + 1}: ')
        respostas = [input(f"Questão {x + 1}:") for x in range(10)]
        aluno['respostas'] = respostas[:]
        cont = 0
        for c in range(len(gabarito)):
            if gabarito[c] == respostas[c]:
                cont += 1
        aluno['nota'] = cont
        aluno['situação'] = sit(cont)
        turma.append(aluno.copy())
        respostas.clear()
    return turma

def mostrarResultados(turma):
    print('- ' * 15)
    for aluno in turma:
        for k, v in aluno.items():
            print(f'{k.title()}: {v}')
        print('- ' * 5)


# Programa principal
gabarito = gerarGabarito()
turma = salvarNotasDosAlunos(gabarito)
mostrarResultados(turma)