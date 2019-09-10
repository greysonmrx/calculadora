# Complete as funcoes a seguir

def soma(a, b):
	# Código para realizar uma soma
	print("\nA soma de {x} + {y} é: {result}".format(x = a, y = b, result = a + b))

def subtrai(a, b):
	# Código para realizar uma subtração
	print("\nA subtração de {x} - {y} é: {result}".format(x = a, y = b, result = a - b))

def multiplica(a, b):
	# Código para realizar uma multiplicação
	print("\nA multiplicação de {x} x {y} é: {result}".format(x = a, y = b, result = a * b))

def divide(a, b):
	# Verificação simples para a calculadora não dividir por zero
	if (b == 0):
		print("\nNão é possível dividir por zero!")
	else:
		# Código para realizar uma divisão
		print("\nA divisão de {x} ÷ {y} é: {result}".format(x = a, y = b, result = a / b))


# Programa principal

print("Calculadora simples")

# Recebendo dois números do usuário
num1 = float(input("Insira o primeiro numero: "))
num2 = float(input("Insira o segundo numero: "))

# Chamando as funções criadas anteriormente
soma(num1, num2)
subtrai(num1, num2)
multiplica(num1, num2)
divide(num1, num2)