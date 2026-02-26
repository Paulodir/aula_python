#importa a biblioteca os (para comandos no terminal)
import os
#Criar uma calculadora com as funções de soma subtração multiplicação e divisão

# Função que recebe 2 numeros e retorna a soma
def somar(a,b):
    #Efetua a soma e armazena em c
    c = a+b
    return c
# Função que recebe 2 numeros e retorna o resultado da subtração 
def subtrair(a,b):
    #Efetua a soma e armazena em c
    c = a-b
    return c

# Função que recebe 2 numeros e retorna o resultado da multiplicação 
def multiplicar(a,b):
    #Efetua a soma e armazena em c
    return a * b

# Função que recebe 2 numeros e retorna o resultado da divisão 
def dividir(a,b):
    # Verifica de o divisor é diferente de zero para evitar erro
   if b!=0:
       # se diferente de 0 efetua a divisão
       return a/b
   else:
       return 'Erro: Divisão por Zero!'
   
# função principal que executa a calculadora

def main():
    while True:
        os.system('cls')
        print('Selecione a operação:')
        print('1. Soma')
        print('2. Subtração')
        print('3. Multiplicação')
        print('4. Divisão')
        print('9. Sair')

        #Recebe a escolha do usuário 
        escolha = input('Digite sua escolha (1/2/3/4):')

        if escolha == '9':
            break
        
        # Recebe os dois numeros da operação
        num1 = float(input('Digite o primeiro número:'))
        num2 = float(input('Digite o segundo número:'))

        resultado = None

        # verifica a escolha do usuario e chama a função 
        if escolha == '1':
            resultado = somar(num1,num2)
        elif escolha == '2':
            resultado = subtrair(num1,num2)
        elif escolha == '3':
            resultado = multiplicar(num1,num2)
        elif escolha == '4':
            resultado = dividir(num1,num2)
        else:
            print('Opção Inválida!')
        
        print('Resultado: ', resultado)

        #aguarda o usuario presionar enter para continuar
        input('Precione enter para continuar')
#só executa a main() de o arquivo for rodado diretamente
if __name__ == "__main__":
    main()