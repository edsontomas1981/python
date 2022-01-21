import json
import os.path
import sys

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    Cuidado para não retornar categorias repetidas.   
    em cada função dar a opção de digitar 0 para voltar (Edson) 
    '''
    ...

def listar_por_categoria(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    em cada função dar a opção de digitar 0 para voltar (Edson)
    '''
    ...
    

def produto_mais_caro(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    em cada função dar a opção de digitar 0 para voltar (Edson)
    '''
    ...


def produto_mais_barato(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    em cada função dar a opção de digitar 0 para voltar (Edson)
    '''
    ...

def top_10_caros(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    em cada função dar a opção de digitar 0 para voltar (Edson)
    '''
    ...

def top_10_baratos(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    em cada função dar a opção de digitar 0 para voltar (Edson)

    '''
    ...

def imprimi_menu () :
    print("Digite uma opção : ")
    print("1. Listar categorias :")
    print("2. Listar produtos de uma categoria :")
    print("3. Produto mais caro por categoria :")
    print("4. Produto mais barato por categoria :")
    print("5. Top 10 produtos mais caros :")
    print("6. Top 10 produtos mais baratos :")
    print("0. Sair :")
    opcao = input("Digite a opção desejada")
    return opcao

def menu(dados):
    
    opcao=imprimi_menu()
    eUmaLetra = opcao.isdigit()
    while opcao > 6 or opcao < 0 or eUmaLetra:
        print("Opção inválida")
        opcao=imprimi_menu()


'''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá, em loop, realizar as seguintes ações:
    - Exibir as seguintes opções:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair
    - Ler a opção do usuário.
    - No caso de opção inválida, imprima uma mensagem de erro.
    - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    - Imprimir o retorno salvo. 
    O loop encerra quando a opção do usuário for 0.
    '''
    
# Programa Principal - não modificar!
d = obter_dados()
menu(d)
