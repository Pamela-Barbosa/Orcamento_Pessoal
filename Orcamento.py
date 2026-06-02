
class Orcamento:
    def __init__(self, dia: str, categoria: str, valor: float):
        self.dia = dia
        self.categoria = categoria
        self.valor = valor

    def __str__(self):

        return f"Orçamento: {self.dia} | Categoria: {self.categoria} | Valor: R$ {self.valor:.2f}"


def normalizar_palavra(texto):
    """Remove espaços, acentos e padroniza para minúsculas."""
    com_acento = "áàãâéêíóôõúçÁÀÃÂÉÊÍÓÔÕÚÇ"
    sem_acento = "aaaaeeioooucaaaaeeiooouc"

    tabela = str.maketrans(com_acento, sem_acento)

    return texto.strip().lower().translate(tabela)

lista_categorias = []
lista_valores = []
opcoes_validas = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"]
opcoes_normalizadas=['segunda', 'terca', 'quarta', 'quinta', 'sexta',"sabado", "domingo"]

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
			print("\n--- Cadastro de Orçamentos ---")
			total_orcam = float(input("Digite o valor em reais do total do orçamento (R$):"))
			limite_alerta = float(input("Digite o limite de alerta em porcentagem (ex: 80): "))
			orcamento = True
		elif menu == 2:
			print("\n--- Cadastro de Despesas ---")
			if not orcamento:
				print("Inválido! O orçamento ainda não foi definido.\nPor favor, escolha a opção 1 para configurar seu limite semanal.\n")
			else:
				while True :
					entrada = input("Digite uma opção: ")
					entrada_tratada = normalizar_palavra(entrada)

					if entrada_tratada in opcoes_normalizadas:
						posicao = opcoes_normalizadas.index(entrada_tratada)
						palavra_correta = opcoes_validas[posicao]
						dia_selecionado = palavra_correta
						break
					else:
						print("Opção inválida! Tente novamente.\n")

				categoria = input("Digite uma categoria: ")
				valor_str = input("Digite um valor: ")
				valor = float(valor_str) # Convert the input string to a float
				print(f"Você escolheu: {palavra_correta}")
				print(f"Você escolheu: {categoria}")
				print(f"Você escolheu: {valor_str}") # Print the original string input for value
				orcamentoObj = Orcamento(dia_selecionado,categoria,valor)
				lista_valores.append(orcamentoObj)
		elif menu == 3:
			print("\n--- Lista de Despesas ---")
			for dia in lista_valores:
				print(dia)
				
			print("\n--- Opções ---")
			print("1. Volta ao Menu Principal")
			sub_menu = input("Digite uma opção: ")
		
	

		elif menu == 7:
			print("\n--- Limpar Despesas ---")
			print("Deseja remover todas as despesas ? ( S , N )")
			confirmacao = input("Digite uma opção: ")
			confirmacao = confirmacao.lower();
			if confirmacao == 'S':
				lista_valores.clear()
				
			print("\n--- Opções ---")
			print("1. Volta ao Menu Principal")
			sub_menu = input("Digite uma opção: ")
		elif menu == 8:
			print("\n--- Sair ---")
			print("Deseja sair do sistema ? ( S , N )")
			confirmacao = input("Digite uma opção: ")
			confirmacao = confirmacao.lower();
			if confirmacao == 's':	
				break	

