import matplotlib.pyplot as plt
import pymysql.cursors


conexao = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="erp",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)

autentico = False
usuarioSupremo = False


def LogarCadastrar():
    usuarioExitente = 0
    autenticado = False
    usuarioMaster = False

    if(decisao == 1):
        nome = input("Digite seu Nome:")
        senha = input("Digite sua Senha:")
    

        for linha in resultado:
            if(nome == linha['nome'] and senha == linha['senha']):
                if(linha['nivel'] == 1):
                    usuarioMaster = False
                elif(linha['nivel'] == 2):
                    usuarioMaster = True
                autenticado = True
                break
            else:
                autenticado = False
        if(not autenticado):
            print("Email ou Senha Inválido!")

    
    elif(decisao == 2):
        print("Faça seu cadastro:")
        nome = input("Digite seu Nome:")
        senha = input("Digite sua Senha:")

        for linha in resultado:
            if(nome == linha['nome'] and senha == linha['senha']):
                usuarioExitente = 1
        
        if(usuarioExitente == 1):
            print("Usuário já cadastrado, tente um nome ou senha diferente!")
        elif(usuarioExitente == 0):
            try:
                with conexao.cursor() as cursor:
                    cursor.execute('insert into cadastros (nome, senha, nivel) values (%s, %s, %s)', (nome, senha, 1))
                    conexao.commit()
                print('usuario cadastrado com sucesso')
            except:
                print('erro ao se cadastrar')
    
    return autenticado, usuarioMaster


def cadastrarProdutos():
    nome = input("Digite o nome do produto: ")
    ingredientes = input("Digite os ingredientes do produto: ")
    grupo = input("Digite o grupo desse produto: ")
    preco = float(input("Digite o Preco: R$"))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('''insert into produtos (nome, ingredientes, grupo, preco)
             values (%s, %s, %s, %s)''', (nome, ingredientes, grupo, preco))
            
            conexao.commit()
            print('produto cadastrado com sucesso')
    except:
        print('erro ao cadastrar produto')


def listarProdutos():
    produtos = []
    produtosCadastrados = {}

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from produtos')
            produtosCadastrados = cursor.fetchall()
    except:
        print('erro ao conectar ao banco de dados')

    for i in produtosCadastrados:
        produtos.append(i)

    if len(produtos) != 0:
        for i in range(0, len(produtos)):
            print(produtos[i])
    else:
        print('nenhum produto cadastrado')


def excluirProdutos():
    idDeletar = int(input("Digite o id do produto que será apagado: "))

    try:
        with conexao.cursor() as cursor:
            cursor.execute("delete from produtos where id = {}".format(idDeletar))
            cursor.commit()
    except:
        print("Erro ao excluir produto")


def listarPedidos():
    pedidos = []
    decision = 0

    while (decision != 2):
        pedidos.clear()
        listaPedidos = {}

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from pedidos')
                listaPedidos = cursor.fetchall()

        except:
            print("ERRO no banco de dados")

        for i in listaPedidos:
            pedidos.append(i)
        
        if(len(pedidos) != 0):
            for i in range(0, len(pedidos)):
                print(pedidos[i])
        else:
            print("Nenhum pedido encontrado...")

        decision = int(input("1 Entregar Produto / 2 voltar"))
        if(decision == 1):
            idDeletar = int(input("Digite o id do produto entregue: "))
            try:
                with conexao.cursor() as cursor:
                    cursor.execute('delete from pedidos where id = {}'.format(idDeletar))
                    print("produto dado como entregue")
            except:
                print("Erro ao dar pedido como entregue")


def gerarEstatistica():
    produtos = 0
    vendido = 0

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from produtos')
            produtos = cursor.fetchall()
    except:
        print('erro ao fazer consulta no banco de dados')

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from estatisticaVendido')
            vendido = cursor.fetchall()
    except:
        print('erro ao fazer a consulta no banco de dados')

    estado = int(input("1 pesquisar por nome\n2 pesquisar por grupo\n0 sair\n:_"))
    if(estado == 1):
        organizar = int(input("1 organizar por custo\n2 organizar por quantidade\n:_"))

        if(organizar == 1):
            valores = []
            valores.clear()
            nomeProdutos = []
            nomeProdutos.clear()
            for i in produtos:
                nomeProdutos.append(i['nome'])
            
            for i in range(0, len(nomeProdutos)):
                somaValor = -1
                for venda in vendido:
                    if (venda['nome'] == nomeProdutos[i]):
                        somaValor += venda['preco']
                if somaValor == -1:
                    valores.append(0)
                elif somaValor > 0:
                    valores.append(somaValor + 1)
            
            plt.plot(nomeProdutos, valores)
            plt.ylabel('Vendas em reais')
            plt.xlabel('Produtos')
            plt.show()

        elif(organizar == 2):
            grupos = []
            grupos.clear()
            for i in produtos:
                grupos.append(i['nome'])
            grupos = sorted(set(grupos))
            
            qntFinal = []
            qntFinal.clear()

            for quant in range(0, len(grupos)):
                quantUnit = 0
                for i in vendido:
                    if(grupos[quant] == i['nome']):
                        quantUnit += 1
                qntFinal.append(quantUnit)

            plt.plot(grupos, qntFinal)
            plt.ylabel('quantidade unitaria vendida')
            plt.xlabel('produtos')
            plt.show()
    
    elif(estado == 2):
        organizar = int(input("1 organizar por custo\n2 organizar por quantidade\n:_"))

        if(organizar == 1):
            valores = []
            valores.clear()
            nomeProdutos = []
            nomeProdutos.clear()
            for i in produtos:
                nomeProdutos.append(i['grupo'])
            
            for i in range(0, len(nomeProdutos)):
                somaValor = -1
                for venda in vendido:
                    if (venda['grupo'] == nomeProdutos[i]):
                        somaValor += venda['preco']
                if somaValor == -1:
                    valores.append(0)
                elif somaValor > 0:
                    valores.append(somaValor + 1)
            
            plt.plot(nomeProdutos, valores)
            plt.xlabel('Produtos')
            plt.ylabel('Vendas em reais')
            plt.show()

        elif(organizar == 2):
            grupos = []
            grupos.clear()
            for i in produtos:
                grupos.append(i['grupo'])
            grupos = sorted(set(grupos))
            
            qntFinal = []
            qntFinal.clear()

            for quant in range(0, len(grupos)):
                quantUnit = 0
                for i in vendido:
                    if(grupos[quant] == i['grupo']):
                        quantUnit += 1
                qntFinal.append(quantUnit)

            plt.plot(grupos, qntFinal)
            plt.ylabel('quantidade unitaria vendida')
            plt.xlabel('produtos')
            plt.show()


while(not autentico):
    decisao = int(input("Digite 1 para Logar e 2 para cadastrar: "))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from cadastros')
            resultado = cursor.fetchall()
    except:
        print("Falha na conexao do banco de dados!")
    
    autentico, usuarioSupremo = LogarCadastrar()

if(autentico == True):
    print("Usuário Autenticado!")

    if(usuarioSupremo == True):
        decisaoUsuario = 1
        while(decisaoUsuario != 0):
            decisaoUsuario = int(input('''
1 Cadastrar Produtos
2 listar Produtos
3 listar Pedidos
4 visualizar estatisticas
0 Sair
'''))
            if(decisaoUsuario == 1):
                cadastrarProdutos()
            elif(decisaoUsuario == 2):
                listarProdutos()
                delete = int(input("Para excluir algum produto, digite 1, para voltar, digite 0:"))
                if(delete == 1):
                    excluirProdutos()
            elif(decisaoUsuario == 3):
                listarPedidos()
            elif(decisaoUsuario == 4):
                gerarEstatistica()