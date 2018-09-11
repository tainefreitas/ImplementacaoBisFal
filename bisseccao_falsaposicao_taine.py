import math
import sys
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

#Definindo funcao de calculo de x linha na falsa posicao
def x_linha_fp(a, b, f_a, f_b):
    resultado =((a*f_b) - (b*f_a))/(f_b-f_a)
    return resultado

def bisseccao_precisao(a, b, prec, funcao_escolhida):
    if(b - a) < prec:
        x_linha = b
    else:
        #Contador de iteracoes
        k = 1
        #M = f(a)
        if funcao_escolhida == 1:
            M = funcao_1(a)
        elif funcao_escolhida == 2:
            M = funcao_2(a)
        elif funcao_escolhida == 3:
            M = funcao_3(a)
        else:
            M = funcao_4(a)
        while True:
            #Calculo do x_linha    
            x_linha = (a+b)/2

            #Auxiliar para teste de M*F(x)
            if funcao_escolhida == 1:
                aux = funcao_1(x_linha)
            elif funcao_escolhida == 2:
                aux = funcao_2(x_linha)
            elif funcao_escolhida == 3:
                aux = funcao_3(x_linha)
            else:
                aux = funcao_4(x_linha)

            print ("Iteracao %d" %k)
            print ("a: %f" %a)
            print ("b: %f" %b)
            print ("x_linha: %f" %x_linha)
            print ("f(x_linha): %f" %aux)

            if M * aux > 0:
                a = x_linha
            else:
                b = x_linha

            #Teste para sair
            if(b-a) <= prec:
                x_linha = (a+b)/2
                break
                
            k=k+1



def bisseccao_iteracoes(a, b, iteracoes, funcao_escolhida):

    #Contador de iteracoes
    k = 1
    #M = f(a)
    if funcao_escolhida == 1:
        M = funcao_1(a)
    elif funcao_escolhida == 2:
        M = funcao_2(a)
    elif funcao_escolhida == 3:
        M = funcao_3(a)
    else:
        M = funcao_4(a)

    while k <= iteracoes:
        #Calculo do x_linha  
        x_linha = (a+b)/2

        #Auxiliar para teste de M*F(x)
        if funcao_escolhida == 1:
            aux = funcao_1(x_linha)
        elif funcao_escolhida == 2:
            aux = funcao_2(x_linha)
        elif funcao_escolhida == 3:
            aux = funcao_3(x_linha)
        else:
            aux = funcao_4(x_linha)

        print ("Iteracao %d" %k)
        print ("a: %f" %a)
        print ("b: %f" %b)
        print ("x_linha: %f" %x_linha)
        print ("f(x_linha): %f" %aux)
        if M * aux > 0:
            a = x_linha
        else:
            b = x_linha
           
        k=k+1

    

def falsaPosicao_precisao(a, b, prec, funcao_escolhida):
    if (b-a) < prec:
        x_linha = b
    else:
        #Definindo f(a)
        if funcao_escolhida == 1:
            aux_1 = funcao_1(a)
        elif funcao_escolhida == 2:
            aux_1 = funcao_2(a)
        elif funcao_escolhida == 3:
            aux_1 = funcao_3(a)
        else:
            aux_1 = funcao_4(a)

       #Definindo f(b)
        if funcao_escolhida == 1:
            aux_2 = funcao_1(b)
        elif funcao_escolhida == 2:
            aux_2 = funcao_2(b)
        elif funcao_escolhida == 3:
            aux_2 = funcao_3(b)
        else:
            aux_2 = funcao_4(b)
        
        #Teste para verificar se as raizes sao a ou b
        if (abs(aux_1) < prec) or (abs(aux_2) < prec):
            x_linha = a
        else:
            k = 1
            #M = f(a)
            if funcao_escolhida == 1:
                M = funcao_1(a)
            elif funcao_escolhida == 2:
                M = funcao_2(a)
            elif funcao_escolhida == 3:
                M = funcao_3(a)
            else:
                M = funcao_4(a)

            while True:
                #Calculo do x_linha
                x_linha = (a*aux_2)-(b*aux_1)/ (aux_2-aux_1)

                #Auxiliar para teste de M*F(x)
                if funcao_escolhida == 1:
                    aux = funcao_1(x_linha)
                elif funcao_escolhida == 2:
                    aux = funcao_2(x_linha)
                elif funcao_escolhida == 3:
                    aux = funcao_3(x_linha)
                else:
                    aux = funcao_4(x_linha)

                print ("Iteracao %d" %k)
                print ("a: %f" %a)
                print ("b: %f" %b)
                print ("x_linha: %f" %x_linha)
                print ("f(x_linha): %f" %aux)

                #Teste de M
                if M * aux > 0:
                    a = x_linha
                else:
                    b = x_linha

                #Teste para sair
                if(b-a) <= prec:
                    x_linha = (a*aux_2)-(b*aux_1)/ (aux_2-aux_1)
                    break
                    
                k=k+1

def falsaPosicao_iteracoes(a, b, iteracoes, funcao_escolhida):
       #Definindo f(a)
        if funcao_escolhida == 1:
            aux_1 = funcao_1(a)
        elif funcao_escolhida == 2:
            aux_1 = funcao_2(a)
        elif funcao_escolhida == 3:
            aux_1 = funcao_3(a)
        else:
            aux_1 = funcao_4(a)

       #Definindo f(b)
        if funcao_escolhida == 1:
            aux_2 = funcao_1(b)
        elif funcao_escolhida == 2:
            aux_2 = funcao_2(b)
        elif funcao_escolhida == 3:
            aux_2 = funcao_3(b)
        else:
            aux_2 = funcao_4(b)
        
        k = 1
        #M = f(a)
        if funcao_escolhida == 1:
            M = funcao_1(a)
        elif funcao_escolhida == 2:
            M = funcao_2(a)
        elif funcao_escolhida == 3:
            M = funcao_3(a)
        else:
            M = funcao_4(a)

        while k <= iteracoes:
            #Calculo do x_linha
            x_linha = (a*aux_2)-(b*aux_1)/ (aux_2-aux_1)

            #Auxiliar para teste de M*F(x)
            if funcao_escolhida == 1:
                aux = funcao_1(x_linha)
            elif funcao_escolhida == 2:
                aux = funcao_2(x_linha)
            elif funcao_escolhida == 3:
                aux = funcao_3(x_linha)
            else:
                aux = funcao_4(x_linha)

            print ("Iteracao %d" %k)
            print ("a: %f" %a)
            print ("b: %f" %b)
            print ("x_linha: %f" %x_linha)
            print ("f(x_linha): %f" %aux)

            #Teste de M
            if M * aux > 0:
                a = x_linha
            else:
                b = x_linha                
            k=k+1


#Menu para escolha de metodo
def menu():
    print("Bem-vindo(a) a calculadora de Bisseccao e Falsa Posicao!\nOpcoes:")
    print("1) Bisseccao (Precisao)")
    print("2) Bisseccao (Iteracoes)")
    print("3) Falsa Posicao (Precisao)")
    print("4) Falsa Posicao (Iteracoes)")
    print("5) Sair")
    escolha = int(input("O que voce deseja fazer? (Digite o numero com a opcao desejada)\n"))

    if escolha == 1:
        a = float(input("Digite o valor inicial do intervalo (a):\n"))
        b = float(input("Digite o valor final do intervalo (b):\n"))
        prec = float(input("Digite a precisao:\n"))
        print("Escolha a funcao:")
        print("1) x^3-9x+5")
        print("2) x^3-9x+3")
        print("3) e^x-3x")
        print("4) 2.75x^3+18x^2-21x-12")
        funcao_escolhida = int (input("Digite a funcao escolhida:\n"))
        if funcao_escolhida == 1:
            bisseccao_precisao(a, b, prec, funcao_escolhida)
        elif funcao_escolhida == 2:
            bisseccao_precisao(a, b, prec, funcao_escolhida)
        elif funcao_escolhida == 3:
            bisseccao_precisao(a, b, prec, funcao_escolhida)
        elif funcao_escolhida == 4:
            bisseccao_precisao(a, b, prec, funcao_escolhida)
        else:
            sys.exit(0)
        
    elif escolha == 2:
        a = float(input("Digite o valor inicial do intervalo (a):\n"))
        b = float(input("Digite o valor final do intervalo (b):\n"))
        iteracoes = int(input("Digite o numero de iteracoes desejado:"))
        print("Escolha a funcao:")
        print("1) x^3-9x+5")
        print("2) x^3-9x+3")
        print("3) e^x-3x")
        print("4) 2.75x^3+18x^2-21x-12")
        funcao_escolhida = int (input("Digite a funcao escolhida:\n"))
        if funcao_escolhida == 1:
            bisseccao_iteracoes(a, b, iteracoes, funcao_escolhida)
        elif funcao_escolhida == 2:
            bisseccao_iteracoes(a, b, iteracoes, funcao_escolhida)
        elif funcao_escolhida == 3:
            bisseccao_iteracoes(a, b, iteracoes, funcao_escolhida)
        elif funcao_escolhida == 4:
            bisseccao_iteracoes(a, b, iteracoes, funcao_escolhida)
        else:
            sys.exit(0)
    elif escolha == 3:
        a = float(input("Digite o valor inicial do intervalo (a):\n"))
        b = float(input("Digite o valor final do intervalo (b):\n"))
        prec = float (input("Digite a precisao\n"))
        print("Escolha a funcao:")
        print("1) x^3-9x+5")
        print("2) x^3-9x+3")
        print("3) e^x-3x")
        print("4) 2.75x^3+18x^2-21x-12")
        funcao_escolhida = int (input("Digite a funcao escolhida:\n"))
        if funcao_escolhida == 1:
            falsaPosicao_precisao(a, b, prec, funcao_escolhida)
        elif funcao_escolhida == 2:
            falsaPosicao_precisao(a, b, prec, funcao_escolhida)
        elif funcao_escolhida == 3:
            falsaPosicao_precisao(a, b, prec, funcao_escolhida)
        elif funcao_escolhida == 4:
            falsaPosicao_precisao(a, b, prec, funcao_escolhida)
        else:
            sys.exit(0)
        
    elif escolha == 4:
        a = float(input("Digite o valor inicial do intervalo (a):\n"))
        b = float(input("Digite o valor final do intervalo (b):\n"))
        iteracoes = int(input("Digite o numero de iteracoes desejado:"))
        print("Escolha a funcao:")
        print("1) x^3-9x+5")
        print("2) x^3-9x+3")
        print("3) e^x-3x")
        print("4) 2.75x^3+18x^2-21x-12")
        funcao_escolhida = int (input("Digite a funcao escolhida:\n"))
        if funcao_escolhida == 1:
            falsaPosicao_iteracoes(a, b, iteracoes, funcao_escolhida)
        elif funcao_escolhida == 2:
            falsaPosicao_iteracoes(a, b, iteracoes, funcao_escolhida)
        elif funcao_escolhida == 3:
            falsaPosicao_iteracoes(a, b, iteracoes, funcao_escolhida)
        elif funcao_escolhida == 4:
            falsaPosicao_iteracoes(a, b, iteracoes, funcao_escolhida)
        else:
            sys.exit(0)
    elif escolha == 5:
        sys.exit(0)
    else:
        print("Opcao Invalida")

menu()