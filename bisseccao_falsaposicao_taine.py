def bisseccao_erro(a, b, prec):
    print(menu)
    return "1"

def bisseccao_iteracoes(a, b, iteracoes):
    print (menu)
    return "2"

def falsaPosicao_erro(a, b, prec):
    print (menu)
    return "3"

def falsaPosicao_iteracoes(a, b, iteracoes):
    print(menu)
    return "4"



#Menu para escolha de metodo
print("Bem-vindo(a) a calculadora de Bisseccao e Falsa Posicao!\nOpcoes:")
print("1) Bisseccao (Precisao)")
print("2) Bisseccao (Iteracoes)")
print("3) Falsa Posicao (Precisao)")
print("4) Falsa Posicao (Iteracoes)")
menu = int(input("O que voce deseja fazer? (Digite o numero com a opcao desejada)\n"))
a = int(input("Digite o valor inicial do intervalo (a):\n"))
b = int(input("Digite o valor final do intervalo (b):\n"))

if menu == 1:
    prec = int(input("Digite a precisao:\n"))
    bisseccao_erro(a, b, prec)
elif menu == 2:
    iteracoes = int(input("Digite o numero de iteracoes desejado:"))
    bisseccao_iteracoes(a, b,iteracoes)
elif menu == 3:
    prec = int (input("Digite a precisao\n"))
    falsaPosicao_erro(a, b, prec)
elif menu == 4:
    iteracoes = int(input("Digite o numero de iteracoes desejado:"))
    falsaPosicao_iteracoes(a, b, iteracoes)
else:
    print("Opcao Invalida")