import math
#Definido o calculo para a funcao 

def bisseccao_erro(a, b, prec):
  
    return "1"

def bisseccao_iteracoes(a, b, iteracoes):
    return "2"

def falsaPosicao_erro(a, b, prec):
    return "3"

def falsaPosicao_iteracoes(a, b, iteracoes):

    return "4"



#Menu para escolha de metodo
def menu():
    print("Bem-vindo(a) a calculadora de Bisseccao e Falsa Posicao!\nOpcoes:")
    print("1) Bisseccao (Precisao)")
    print("2) Bisseccao (Iteracoes)")
    print("3) Falsa Posicao (Precisao)")
    print("4) Falsa Posicao (Iteracoes)")
    escolha = int(input("O que voce deseja fazer? (Digite o numero com a opcao desejada)\n"))
    a = int(input("Digite o valor inicial do intervalo (a):\n"))
    b = int(input("Digite o valor final do intervalo (b):\n"))

    if escolha == 1:
        prec = int(input("Digite a precisao:\n"))
        bisseccao_erro(a, b, prec)
    elif escolha == 2:
        iteracoes = int(input("Digite o numero de iteracoes desejado:"))
        bisseccao_iteracoes(a, b,iteracoes)
    elif escolha == 3:
        prec = int (input("Digite a precisao\n"))
        falsaPosicao_erro(a, b, prec)
    elif escolha == 4:
        iteracoes = int(input("Digite o numero de iteracoes desejado:"))
        falsaPosicao_iteracoes(a, b, iteracoes)
    else:
        print("Opcao Invalida")

menu()