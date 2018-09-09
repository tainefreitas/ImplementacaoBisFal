import math
#Definido o calculo para a funcao 1
def funcao_1(x):
    resultado = x**3-(9*x)+5
    return resultado

#Definindo o calculo para a funcao 2
def funcao_2(x):
    resultado = x**3-(9*x) +3
    return resultado

#Definindo o calculo para a funcao 3
def funcao_3(x):
    resultado = math.exp(x)-3*x
    return resultado

#Definindo o calculo para a funcao 4
def funcao_4(x):
    resultado = (2.75*x**3)+(18*x**2)-(21*x)-12
    return resultado

#Definindo funcao de calculo de x linha na bisseccao
def x_linha_bis(a,b):
    resultado = (a+b)/2
    return resultado

#Definindo funcao de calculo de x linha na falsa posicao
def x_linha_fp(a, b, f_a, f_b):
    resultado =((a*f_b) - (b*f_a))/(f_b-f_a)
    return resultado




#def bisseccao_erro(a, b, prec):
  
    

#def bisseccao_iteracoes(a, b, iteracoes):
    

#def falsaPosicao_erro(a, b, prec):
    


#def falsaPosicao_iteracoes(a, b, iteracoes):



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
        #bisseccao_erro(a, b, prec)
    elif escolha == 2:
        iteracoes = int(input("Digite o numero de iteracoes desejado:"))
        #bisseccao_iteracoes(a, b,iteracoes)
    elif escolha == 3:
        prec = int (input("Digite a precisao\n"))
        #falsaPosicao_erro(a, b, prec)
    elif escolha == 4:
        iteracoes = int(input("Digite o numero de iteracoes desejado:"))
        #falsaPosicao_iteracoes(a, b, iteracoes)
    else:
        print("Opcao Invalida")

menu()