# Orcamento_Pessoal




### Passo 1: Preparando o Terreno (Fora do While)
* **Criar as Listas de Armazenamento:** Como não podemos usar dicionários, usaremos **listas paralelas** que se conectam pelo mesmo índice:
  * `lista_dias = []`
  * `lista_categorias = []`
  * `lista_valores = []`
* **Criar variáveis de controle de Orçamento:**
  * `orcamento_definido = False`
  * `valor_orcamento = 0.0`
  * `porcentagem_alerta = 0.0`

### Passo 2: O Menu (`while menu_ativo:`)
* Mostrar as 8 opções claramente na tela.
* Receber a escolha do usuário: `opcao = input("Escolha uma opção: ")`

### Passo 3: Implementando a Lógica de Cada Opção

#### Opção 1: Definir Orçamento
* Perguntar o valor total do orçamento (converter para `float`).
* Perguntar o limite de alerta em % (ex: 80) (converter para `float`).
* Mudar `orcamento_definido = True`.

#### Trava de Segurança (Antes das Opções 2 a 6)
* Em cada uma das opções de 2 a 6, a primeira linha deve ser:
  `if not orcamento_definido:` -> Avisar que precisa ir na Opção 1 primeiro.
  `else:` -> Segue para a lógica abaixo.

#### Opção 2: Registrar Nova Despesa (Como resolver seu gap de inputs)
* **Validar o Dia:** Criar um loop `while True` interno que pede o dia. Se o usuário digitar algo diferente de segunda, terça, etc., mandar digitar de novo. *Dica: Use `.lower().strip()` para padronizar sem acentos.*
* **Categoria:** Input simples de texto livre.
* **Valor:** Input convertido para `float`.
* **Guardar:** Dar `.append()` de cada informação nas suas respectivas listas.

#### Opção 3: Listar Despesas (Formato Tabular)
* Usar um loop `for i in range(len(lista_valores)):`
* Imprimir usando f-strings alinhadas. Exemplo: `print(f"{lista_dias[i]:<15} | {lista_categorias[i]:<20} | R$ {lista_valores[i]:>8.2f}")`

#### Opção 4: Resumo por Categoria
* Descobrir as categorias únicas (você pode fazer isso criando uma lista auxiliar de categorias já vistas durante um loop `for`).
* Para cada categoria encontrada, somar os valores correspondentes e calcular a `%` em relação ao orçamento total.

#### Opção 5: Verificar Situação do Orçamento
* Somar todos os valores da `lista_valores` (usando um loop `for`).
* Calcular quanto restou: `restante = valor_orcamento - total_gasto`.
* Calcular a porcentagem gasta atual: `porcentagem_gasta = (total_gasto / valor_orcamento) * 100`.
* Se `porcentagem_gasta >= porcentagem_alerta`, exibir o **Aviso de Alerta Crítico**.

#### Opção 6: Estatísticas dos Dias
* Criar uma lista com os 7 dias da semana padronizados.
* Criar uma lógica para somar os gastos de cada dia individualmente.
* Descobrir qual dia teve a maior soma, menor soma (ignorando dias com gasto zero) e fazer a média dividida apenas pela quantidade de dias que tiveram registros.

#### Opção 7: Resetar Dados (Sua dúvida sobre como fazer)
* Fazer um input: `confirmacao = input("Deseja mesmo limpar todos os dados? (S/N): ").upper()`
* Se for `"S"`, usar o método `.clear()` nas suas listas:
  * `lista_dias.clear()`
  * `lista_categorias.clear()`
  * `lista_valores.clear()`
  * Mudar `orcamento_definido = False` para bloquear o sistema de novo.

#### Opção 8: Sair
* Mudar `menu_ativo = False`.

#### Bloco `else` Geral
* Se o usuário digitar qualquer coisa diferente de 1 a 8: `print("Opção inválida!")`
"""

