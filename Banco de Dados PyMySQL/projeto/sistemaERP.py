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
            decisaoUsuario = int(input("\n1 Cadastrar Produtos:\n2 listar Produtos\n0 Sair\n_"))

            if(decisaoUsuario == 1):
                cadastrarProdutos()
            elif(decisaoUsuario == 2):
                listarProdutos()
                delete = int(input("Para excluir algum produto, digite 1, para voltar, digite 0:"))
                if(delete == 1):
                    excluirProdutos()

