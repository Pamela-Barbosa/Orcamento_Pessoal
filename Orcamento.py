def normalizar_palavra(texto):
    texto = texto.strip().lower()
    com_acento = "áàãâéêíóôõúç"
    sem_acento = "aaaaeeiooouc"
    
    novo_texto = ""
    for letra in texto:
        if letra in com_acento:
            indice = com_acento.index(letra)
            novo_texto += sem_acento[indice]
        else:
            novo_texto += letra
            
    return novo_texto

lista_despesas = []  
opcoes_validas = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"]
opcoes_normalizadas = ["segunda", "terca", "quarta", "quinta", "sexta", "sabado", "domingo"]

orcamento_definido = False
total_orcam = 0.0
limite_alerta = 0.0

menu = 1

while menu != 8:
    print("\n--- MENU Orçamento Pessoal ---")
    print("1. Definir Orçamento")
    print("2. Registrar Nova Despesa")
    print("3. Listar Despesas")
    print("4. Resumo Por Categorias")
    print("5. Verificar Orçamento")
    print("6. Estatísticas Dos Dias")
    print("7. Resetar Dados")
    print("8. Sair")

    entrada_menu = input("Digite uma opção (1 a 8): ")
    
    if entrada_menu.isdigit():
        menu = int(entrada_menu)
        if menu > 8 or menu < 0:
            print("\nOpção inválida! Digite um número.")
            continue
    else:
        print("\nOpção inválida! Digite um número.")
        continue

    if menu == 1:
        print("\n--- Cadastro de Orçamentos ---")
        entrada_total = input("Digite o valor em reais do total do orçamento (R$): ")
        entrada_limite = input("Digite o limite de alerta em porcentagem (ex: 80): ")
        
        total_orcam = float(entrada_total)
        limite_alerta = float(entrada_limite)
        orcamento_definido = True
        print("Orçamento configurado com sucesso!")

    elif menu == 2:
        print("\n--- Cadastro de Despesas ---")
        if not orcamento_definido:
            print("Inválido! O orçamento ainda não foi definido.")
            print("Por favor, escolha a opção 1 para configurar seu limite semanal.\n")
        else:
            dia_selecionado = ""
            while True:
                entrada = input("Digite uma opção da semana (Segunda, Terça, Quarta, ...): ")
                entrada_tratada = normalizar_palavra(entrada)

                if entrada_tratada in opcoes_normalizadas:
                    posicao = opcoes_normalizadas.index(entrada_tratada)
                    dia_selecionado = opcoes_validas[posicao]
                    break
                else:
                    print("Opção inválida! Tente novamente.\n")

            categoria = input("Digite uma categoria: ").strip().capitalize()
            valor = float(input("Digite um valor: "))

            nova_despesa = [dia_selecionado, categoria, valor]
            lista_despesas.append(nova_despesa)
            
            print(f"\nDespesa registrada: {dia_selecionado} | {categoria} | R$ {valor:.2f}")

    elif menu == 3:
        print("\n--- Lista de Despesas ---")
        if len(lista_despesas) == 0:
            print("Nenhuma despesa cadastrada ainda.")
        else:
            print(f"{'Dia':<12} | {'Categoria':<20} | {'Valor':>10}")
            print("-" * 50)
            
            for despesa in lista_despesas:
                dia_str = despesa[0]
                cat_str = despesa[1]
                val_float = despesa[2]
                print(f"{dia_str:<12} | {cat_str:<20} | R$ {val_float:>8.2f}")
            
        input("Digite qualquer tecla para voltar: ")

    elif menu == 4:
        print("\n--- Resumo por Categoria ---")
        if not orcamento_definido:
            print("Inválido! O orçamento ainda não foi definido.")
        elif len(lista_despesas) == 0:
            print("Nenhuma despesa cadastrada ainda.")
        else:
            resumo_categorias = []
            
            for despesa in lista_despesas:
                cat_atual = despesa[1]
                val_atual = despesa[2]
                
                categoria_encontrada = False
                
                for item_resumo in resumo_categorias:
                    if item_resumo[0] == cat_atual:
                        item_resumo[1] = item_resumo[1] + val_atual 
                        categoria_encontrada = True
                        break
                
                if not categoria_encontrada:
                    resumo_categorias.append([cat_atual, val_atual])

            print(f"\n{'Categoria':<20} | {'Total Gasto':>15} | {'% do Orçamento':>15}")
            print("-" * 56)

            for item in resumo_categorias:
                cat = item[0]
                tot = item[1]
                
                if total_orcam > 0:
                    porcentagem = (tot / total_orcam) * 100
                else:
                    porcentagem = 0.0
                    
                print(f"{cat:<20} | R$ {tot:>12.2f} | {porcentagem:>14.2f}%")

        input("Digite qualquer tecla para voltar: ")
    elif menu == 5:
        print("\n--- Verificar Situação do Orçamento ---")
        
        if not orcamento_definido:
            print("Inválido! O orçamento ainda não foi definido.")
            print("Por favor, escolha a opção 1 para configurar seu limite semanal.\n")
        else:
            total_gasto = 0.0
            for despesa in lista_despesas:
                total_gasto += despesa[2]
            
            restante = total_orcam - total_gasto
            
            if total_orcam > 0:
                porcentagem_gasta = (total_gasto / total_orcam) * 100
            else:
                porcentagem_gasta = 0.0
            
            print(f"Total Gasto:     R$ {total_gasto:>8.2f}")
            print(f"Restante:        R$ {restante:>8.2f}")
            print("-" * 40)
            
            if total_gasto > total_orcam:
                print("Atenção!: Você estourou totalmente o seu orçamento!")
            elif porcentagem_gasta >= limite_alerta:
                print("CUIDADO: Você atingiu ou ultrapassou o seu limite de alerta!")
            else:
                print("TRANQUILO: Seus gastos estão abaixo do limite de alerta.")

        input("Digite qualquer tecla para voltar: ")
    elif menu == 6:
        print("\n--- Estatísticas Dos Dias ---")
        if not orcamento_definido:
            print("Inválido! O orçamento ainda não foi definido.")
            print("Por favor, escolha a opção 1 para configurar seu limite semanal.\n")
        elif len(lista_despesas) == 0:
            print("Nenhuma despesa cadastrada ainda.")
        else:
        
            resumo_dias = []
            
            for despesa in lista_despesas:
                dia_atual = despesa[0]
                val_atual = despesa[2]
                
                dia_encontrado = False
                
                for item_dia in resumo_dias:
                    if item_dia[0] == dia_atual:
                        item_dia[1] = item_dia[1] + val_atual
                        dia_encontrado = True
                        break
                
                if not dia_encontrado:
                    resumo_dias.append([dia_atual, val_atual])
            
            
            dia_maior = resumo_dias[0][0]
            maior_valor = resumo_dias[0][1]
            
            dia_menor = resumo_dias[0][0]
            menor_valor = resumo_dias[0][1]
            
            soma_total = 0.0
            
            for item in resumo_dias:
                dia = item[0]
                valor = item[1]
                
                soma_total = soma_total + valor
                
                if valor > maior_valor:
                    maior_valor = valor
                    dia_maior = dia
                    
                if valor < menor_valor:
                    menor_valor = valor
                    dia_menor = dia
            
            qtd_dias_com_gasto = len(resumo_dias)
            media_diaria = soma_total / qtd_dias_com_gasto
            
            print(f"Dias com gastos registrados: {qtd_dias_com_gasto}")
            print(f"Média de gasto diário:     R$ {media_diaria:.2f}")
            print("-" * 45)
            print(f"Dia de MAIOR gasto: {dia_maior} (R$ {maior_valor:.2f})")
            print(f"Dia de MENOR gasto: {dia_menor} (R$ {menor_valor:.2f})")

        input("Digite qualquer tecla para voltar: ")
    elif menu == 7:
        print("\n--- Limpar Despesas ---")
        confirmacao = input("Deseja remover todas as despesas? (S/N): ")
        if normalizar_palavra(confirmacao) == 's':
            lista_despesas.clear()
            orcamento_definido = False
            total_orcam = 0.0
            limite_alerta = 0.0
            print("Todos os dados de despesas foram resetados!")
        input("Digite qualquer tecla para voltar: ")
    elif menu == 8:
        print("\n--- Sair ---")
        confirmacao = input("Deseja sair do sistema? (S/N): ")
        if normalizar_palavra(confirmacao) == 's':
            print("Sistema encerrado. Até mais!")
            break