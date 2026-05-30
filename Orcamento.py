import sys
sys.stdout.reconfigure(encoding='utf-8')

lista_dias = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
lista_categorias = []
lista_valores = []

orcamento = False
menu = 1

while menu <= 8:
		print("\n--- MENU Orçamento Pessoal ---")
		print("1. Definir Orçamento")
		print("2. Registrar Nova Despesa")
		print("3. Listar Despesa")
		print("4. Resumo Por Categorias")
		print("5. Verificar Orçamento")
		print("6. Estatísticas Dos Dias ")
		print("7. Resetar Dados")
		print("8. Sair")

		menu = int(input("Digite uma opção (1 a 8): "))
		if menu == 1:
			total_orcam = float(input("Digite o valor em reais do total do orçamento (R$):"))
			limite_alerta = float(input("Digite o limite de alerta em porcentagem (ex: 80): "))
			orcamento = True
		elif menu == 2:
			if not orcamento:
				print("Inválido! O orçamento ainda não foi definido.\nPor favor, escolha a opção 1 para configurar seu limite semanal.\n")
			else:
				while True :
					for dias in range(len(lista_dias)):
						print(lista_dias[dias])

					dia = input("Digite um dia da semana: ")
					if(dia):
						break

					

