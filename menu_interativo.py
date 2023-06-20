import sqlite3 # importa a pasta SQL  para dentro do python
from proj_minhas_funcoes import *

conexao = sqlite3.connect("sistemaVendasJunior.sqlite3") # Conecta o banco de dados com Python
##################################################

while True:
    print("----- Sistema de Vendas do Junior -----")
    print("Selecione a opção desejada: 1) Cadastrar Clientes, 2) Mostrar Clientes, 3) Mostrar Marcas, 4) Adicionar produto ao estoque  0) Sair")
    opcao = int(input("Selecione: "))
    if opcao == 0:
        print("Programa finalizado!")
        break
    elif opcao == 1: #Cadastro de Clientes
        cadastrar_cliente(conexao)
    elif opcao == 2: #Mostrar Clientes
        mostrar_clientes(conexao)
    elif opcao == 3: #Mostrar Marcas
        mostrar_marcas(conexao)
    elif opcao == 4: #Adicionar produto
        add_produtos(conexao)
    else:
        print("Opção inválida!")

##################################################
conexao.commit() # A função “commit”, associada à variável “conexao”, chamada logo em seguida, 
                 # serve para efetivamente salvar as alterações realizadas no banco de dados. 
conexao.close()  # é chamada para fechar a conexão