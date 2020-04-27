from os import system , name


def limparTela():
	"""
	Função responsável pela limpeza e tela no terminal.
	"""
	if name == 'nt':
		system ('cls ')
	else:
		system ('clear ')


def menu(n100=1, n50=1, n20=2, n10=1, n5=1, n2=1, n1=1):
	""" 
	Esta função exibe na tela o menu de funções do caixa eletrônico e realiza
	a seleção das tarefas
	"""
	#a variável somatorio pega os valores das notas e realiza, como o próprio
	#nome já diz, o somatório do dinheiro. Como as notas estão em unidades
	#será necessário a realização da multiplicação pelo valor da nota corres-
	#pondente.
	somatorio = somarNotas(n100*100, n50*50, n20*20, n10*10, n5*5, n2*2, n1*1)
	limparTela()
	print('-' * 38)
	print("1 - Depositar")
	print("2 - Sacar")
	print("3 - Saldo")
	print("4 - Relatório")
	print("5 - Finalizar")
	print('-' * 38)
	esc = int(input("Escolha uma opcao: "))
	if esc == 1:
		print("-- Para encerrar o depósito digite um valor negativo --")
		depositar(n100, n50, n20, n10, n5, n2, n1)
	elif esc == 2:
		sacar(n100, n50, n20, n10, n5, n2, n1, somatorio)
	elif esc == 3:
		saldo(n100, n50, n20, n10, n5, n2, n1, somatorio)
	elif esc == 4:
		relatorio(n100, n50, n20, n10, n5, n2, n1, somatorio)
	elif esc == 5:
		saqueFinal(n100, n50, n20, n10, n5, n2, n1, somatorio)


def depositar(n100, n50, n20, n10, n5, n2, n1, valorDp=0):
	"""
	Esta função é responsável pelo deposito de dinheiro do usuário.
	"""
	valor = int(input("Coloque o dinheiro: R$"))
	#Dado um valor correspondende pelo usuário e se tal valor for maior
	#ou igual a 0, será executado os seguintes trechos abaixo:
	if valor >= 0:
		if valor == 100:
			#Será somado +1 para cada nota e +n na variável valorDp, onde n
			#significa o valor em questão da nota sendo acumulado.
			return depositar(n100+1, n50, n20, n10, n5, n2, n1, valorDp+100)
		elif valor == 50:
			return depositar(n100, n50+1, n20, n10, n5, n2, n1, valorDp+50)
		elif valor == 20:
			return depositar(n100, n50, n20+1, n10, n5, n2, n1, valorDp+20)
		elif valor == 10:
			return depositar(n100, n50, n20, n10+1, n5, n2, n1, valorDp+10)
		elif valor == 5:
			return depositar(n100, n50, n20, n10, n5+1, n2, n1, valorDp+5)
		elif valor == 2:
			return depositar(n100, n50, n20, n10, n5, n2+1, n1, valorDp+2)
		elif valor == 1:
			return depositar(n100, n50, n20, n10, n5, n2, n1+1, valorDp+1)
		else:
			print("Nota de {:.2f} não reconhecida".format(valor))
			return depositar(n100, n50, n20, n10, n5, n2, n1, valorDp)
	else:
		print("Valor depositado: R${:.2f}".format(valorDp))
		esc = str(input("--> Enter para continuar..."))
		if not esc:
			return menu(n100, n50, n20, n10, n5, n2, n1)


def mostrarNotas(n100=0, n50=0, n20=0, n10=0, n5=0, n2=0, n1=0):
	"""
	Função responsável por mostrar as notas na tela logo após o saque do dinheiro.
	"""

	if n100 > 0:
		#De inicio será mostrado os valores na tela, caso n100
		#seja maior do que 0.
		print("R$100,00")
		#Após exibir o valor, será subtraido até que n100 deixe de
		#ser maior do que 0 e assim, a função segue recursivamente
		#analogamente para todos os casos, mostrando na tela todos
		#os valores.
		return mostrarNotas(n100-1, n50, n20, n10, n5, n2, n1)
	elif n50 > 0:
		print("R$50,00")
		return mostrarNotas(n100, n50-1, n20, n10, n5, n2, n1)
	elif n20 > 0:
		print("R$20,00")
		return mostrarNotas(n100, n50, n20-1, n10, n5, n2, n1)
	elif n10 > 0:
		print("R$10,00")
		return mostrarNotas(n100, n50, n20, n10-1, n5, n2, n1)
	elif n5 > 0:
		print("R$5,00")
		return mostrarNotas(n100, n50, n20, n10, n5-1, n2, n1)
	elif n2 > 0:
		print("R$2,00")
		return mostrarNotas(n100, n50, n20, n10, n5, n2-1, n1)
	elif n1 > 0:
		print("R$1,00")
		return mostrarNotas(n100, n50, n20, n10, n5, n2, n1-1)


def verificarSaque(n100, n50, n20, n10, n5, n2, n1, valor, valorSq=0, v100=0, v50=0, v20=0, v10=0, v5=0, v2=0, v1=0):
	"""
	Verifica e calcula as cada nota para realização do eventual saque do usuário.
	"""
	if valorSq < valor:
		#É Verificado se o valorSq(valor de saque) for menor que o valor para a execução dos trechos abaixo, pois enquanto 
		#o valorSq for menor, ele será acumulado com a respectiva nota, fazendo a condição parar quando o valorSq for 
		#maior ou igual ao valor.
		if valor - valorSq >= 100 and n100 > 0:
			#Para realização do saque será decrementado 1 da respectiva nota, o valorSq será acumulado recursivamente e
			#será usado uma variável auxiliadora com inicial da letra 'v', como por exemplo a variável v100 que assim como
			#todas as outras auxiliadoras tem o papel de incrementar +1, fazendo um controle correto entre as notas que são
			#sacadas e os valores que serão mostrados na tela das notas que sobraram.
			return verificarSaque(n100-1, n50, n20, n10, n5, n2, n1, valor, valorSq+100, v100+1, v50, v20, v10, v5, v2, v1)
		elif valor - valorSq >= 50 and n50 > 0:
			return verificarSaque(n100, n50-1, n20, n10, n5, n2, n1, valor, valorSq+50, v100, v50+1, v20, v10, v5, v2, v1)
		elif valor - valorSq >= 20 and n20 > 0:
			return verificarSaque(n100, n50, n20-1, n10, n5, n2, n1, valor, valorSq+20, v100, v50, v20+1, v10, v5, v2, v1)
		elif valor - valorSq >= 10 and n10 > 0:
			return verificarSaque(n100, n50, n20, n10-1, n5, n2, n1, valor, valorSq+10, v100, v50, v20, v10+1, v5, v2, v1)
		elif valor - valorSq >= 5 and n5 > 0:
			return verificarSaque(n100, n50, n20, n10, n5-1, n2, n1, valor, valorSq+5, v100, v50, v20, v10, v5+1, v2, v1)
		elif valor - valorSq >= 2 and n2 > 0:
			return verificarSaque(n100, n50, n20, n10, n5, n2-1, n1, valor, valorSq+2, v100, v50, v20, v10, v5, v2+1, v1)
		elif valor - valorSq >= 1 and n1 > 0:
			return verificarSaque(n100, n50, n20, n10, n5, n2, n1-1, valor, valorSq+1, v100, v50, v20, v10, v5, v2, v1+1)
		else:
			print("Não temos notas suficiente para esse saque")
			esc = str(input("--> Enter para continuar..."))
			if not esc:
				return n100 + v100, n50 + v50, n20 + v20, n10 + v10, n5 + v5, n2 + v2, n1 + v1
	else:
		print("Pegue seu dinheiro:")
		mostrarNotas(v100, v50, v20, v10, v5, v2, v1)
		esc = str(input("--> Enter para continuar..."))
		if not esc:
			return menu(n100, n50, n20, n10, n5, n2, n1)
		return n100, n50, n20, n10, n5, n2, n1


def sacar(n100, n50, n20, n10, n5, n2, n1, total):
	"""
	Função que realiza o saque das notas dado um valor pelo usuário.
	"""
	print("Notas disponíveis na maquina")
	#Inicialmente será exibido o estoque de notas na tela.
	estoque(n100, n50, n20, n10, n5, n2, n1)
	print('-' * 38)
	#Em seguida será pedido um valor do usuário que passará por verificações para
	#a chamada das respectivas funções.
	valor = int(input("Digite o valor a ser sacado: R$"))
	if valor <= total:
		n100, n50, n20, n10, n5, n2, n1 = verificarSaque(n100, n50, n20, n10, n5, n2, n1, valor)
		return menu(n100, n50, n20, n10, n5, n2, n1)

	elif total < valor:
		print("Saldo insuficiente. Temos apenas R${:.2f} em caixa".format(total))
		esc = str(input("Deseja sacar esse valor (S/N)? "))
		if esc == "s" or esc == "S":
			#A váriavel valor (onde possui os dados de entrada do usuário), será substituida pelo
			#valor da variável total do caixa.
			valor = total
			n100, n50, n20, n10, n5, n2, n1 = verificarSaque(n100, n50, n20, n10, n5, n2, n1, valor)
			return menu(n100, n50, n20, n10, n5, n2, n1)
		else:
			return menu(n100, n50, n20, n10, n5, n2, n1)


def saqueFinal(n100, n50, n20, n10, n5, n2, n1, total):
	"""
	Função que exibe a última operação de saque na tela para o usuário
	"""
	esc = str(input("Deseja sacar os {} antes de fechar (S/N)? ".format(total)))
	if esc == "s" or esc == "S":
		mostrarNotas(n100, n50, n20, n10, n5, n2, n1)
		esc = str(input("--> Enter para finalizar..."))
		if not esc:
			exit()
	else:
		return menu(n100, n50, n20, n10, n5, n2, n1)


def saldo(n100,n50,n20,n10,n5,n2,n1, somatorio):
	"""
	Esta função exibe o saldo atual do usuário na tela
	"""
	print("Saldo atual: R${:.2f}".format(somatorio))
	esc = str(input("--> Enter para continuar..."))
	if not esc:
		return menu(n100, n50, n20, n10, n5, n2, n1)


def relatorio(n100, n50, n20, n10, n5, n2, n1, somatorio):
	"""
	Esta função exibe o relatório das tarefas executadas pela máquina na tela
	"""
	print("+-------------------------+")
	print("|     Relatório geral     |")
	print("+-------------------------+")
	print("Notas de R$100,00: {}".format(n100))
	print("Notas de R$50,00: {}".format(n50))
	print("Notas de R$20,00: {}".format(n20))
	print("Notas de R$10,00: {}".format(n10))
	print("Notas de R$5,00: {}".format(n5))
	print("Notas de R$2,00: {}".format(n2))
	print("Notas de R$1,00: {}".format(n1))
	print("Saldo total: R${:.2f}".format(somatorio))
	esc = str(input("--> Enter para continuar..."))
	if not esc:
		return menu(n100, n50, n20, n10, n5, n2, n1)


def estoque(n100, n50, n20, n10, n5, n2, n1):
	"""
	Esta função exibe as notas disponíveis na máquina na tela 
	quando a função saque for chamada
	"""
	if n100 >= 1:
		print("{} x R$100,00".format(n100))
	if n50 >= 1:
		print("{} x R$50,00".format(n50))
	if n20 >= 1:
		print("{} x R$20,00".format(n20))
	if n10 >= 1:
		print("{} x R$10,00".format(n10))
	if n5 >= 1:
		print("{} x R$5,00".format(n5))
	if n2 >= 1:
		print("{} x R$2,00".format(n2))
	if n1 >= 1:
		print("{} x R$1,00".format(n1))


def somarNotas(n100,n50,n20,n10,n5,n2,n1):
	"""
	Esta função realiza o somatório das notas
	"""
	return n100+n50+n20+n10+n5+n2+n1


def main():
	menu()


main()
