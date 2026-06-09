Contexto: Uma pessoa deseja controlar suas despesas semanais para não ultrapassar um limite definido. O programa deve permitir o registro diário de gastos, análise por categoria e alertas quando o total se aproxima do limite.

1.Menu inicial (loop infinito até sair):
2.Definir orçamento semanal e limite de alerta (em %).
3.Registrar nova despesa (dia da semana, categoria, valor).
4.Listar todas as despesas registradas (formato tabular simples com f-strings).
5.Resumo por categoria (mostrar categoria, total gasto e % do orçamento total).
6.Verificar situação do orçamento (total gasto, restante, se ultrapassou ou está abaixo do limite de alerta).
7.Estatísticas dos dias (qual dia teve maior gasto, qual teve menor, média diária).
8.Resetar todos os dados (limpar listas após confirmação).
Sair.
Comportamento esperado:

* Ao iniciar, se não houver orçamento definido, as opções 2-6 devem avisar que é necessário definir o orçamento primeiro.
* O limite de alerta é um percentual (ex: 80%). Se o total gasto atingir ou ultrapassar esse percentual do orçamento, a opção 5 deve exibir um aviso.
* Categorias são strings livres digitadas pelo usuário (ex: "Alimentação", "Transporte").
* Dias da semana devem ser validados: apenas "segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo" (aceitar com ou sem acento, mas armazenar padronizado).
* A opção 4 deve iterar sobre as despesas, acumular por categoria e exibir uma linha por categoria encontrada.
* A opção 6 deve calcular o total por dia (usando loop), identificar o maior e o menor, e a média de gasto por dia (considere apenas dias que tiveram gastos, não todos os 7).
* A opção 7 deve pedir confirmação ("S" ou "N") antes de limpar.