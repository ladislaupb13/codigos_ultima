"""
A Primeira coisa a se fazer ao criar uma classe é usar a função __init__():

__init__(): 
- Essa função tem a função de iniciar a classe
- Dentro dessa função tem que ter as caracteristicas que estarão presentes na classe
    Ex: Cliente
    - NOME
    - CPF
    - IDADE
    - ENDEREÇO

self = faz referencia ao objeto "É O PROPIO OBJETO"

uso para qualquer instancia do objeto

self.instancia

ex: self.cor
    self.cpf
e assim sucessivamente...


Para criar um objeto em um codigo, basta atribuir uma variavel a uma classe

Ex:

"""

import sqlite3 # importa a pasta SQL  para dentro do python

conexao = sqlite3.connect("sistemaVendasJunior.sqlite3")

def mostrar_marcas(conexao):
    cursor = conexao.cursor()

    comando = f"""
    SELECT * FROM Marcas;
    """
     
    marcas = cursor.execute(comando)
    for marca in marcas:
        print(marca)

class ClienteESP:
    def __init__(self, conexao):
        self.nome = None
        self.cpf = None
        self.idade = None
        self.endereco = None
        self.telefone = None
        self.conexao = conexao
        self.cursor = conexao.cursor()
    def cadastro(self):
        self.nome = input("Olá, Por favor, Digite seu NOME: ")
        self.cpf = input("Digite o seu numero do CPF: ")
        self.idade = int(input("Digite a sua idade: "))
        self.telefone = int(input("Digite seu telefone: "))
        self.endereco = input("Digite o seu endereço")

        comando = f"""
        INSERT INTO Clientes (nome, cpf, telefone, endereco) VALUES (?, ?, ?, ?)
        """
        valores = [self.nome, self.cpf, self.telefone, self.endereco]
        self.cursor.execute(comando, valores)
        self.conexao.commit()
    def add_produtos(self):
        tipo = input("Qual o tipo do seu produto? ")
        preco = input("Qual o preço do seu produto? ")
        qtd_estoque = input("Quantos produtos tem no seu estoque? ")
        mostrar_marcas(conexao)
        marca_id = int(input("Digite o id da marca: "))

    
        comando = f"""INSERT INTO Produto (tipo, preco, qtd_estoque, marca_id) VALUES(?,?,?,?)"""

        valores = [tipo, preco, qtd_estoque,marca_id]

        self.cursor.execute(comando, valores)
        self.conexao.commit()


cliente = ClienteESP(conexao)
cliente.cadastro()

conexao.commit()
conexao.close() 

