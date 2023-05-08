### Calculadora

while True:
    
    valor1 = input("Digite um número: ")
    operador = input("Escolha um operador (+ - / *): ")
    valor2 = input("Digite outro número: ")
    
    numeros_validos = None
    operadores_permitidos = '+-/*'

    try:
        valor1float = float(valor1)
        valor2float = float(valor2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Um ou ambos os números são inválidos.")
        continue

    if operador not in operadores_permitidos:
        print("Digite um operador válido.")
        continue
    
    valor1float = float(valor1)
    valor2float = float(valor2)

    if operador == str("+"):
        print("O resultado da soma é: " f'{valor1float + valor2float}')

    elif operador == str("-"):
        print("O resultado da subtração é: " f'{valor1float - valor2float}')
    
    elif operador == str("/"):
        print("O resultado da divisão é: " f'{valor1float / valor2float}')

    elif operador == str("*"):
        print("O resultado da multiplicação é: " f'{valor1float * valor2float}')