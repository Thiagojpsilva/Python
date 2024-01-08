"""
# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
"""
from datetime import datetime
from dateutil.relativedelta import relativedelta
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

valor_total = 1_000_000
data_empretimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_empretimo + delta_anos

data_parcelas = []
data_parcela = data_empretimo
while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

numero_parcelas = len(data_parcelas)
valor_parcela = valor_total / numero_parcelas

for data in data_parcelas:
    print(data.strftime('%d/%m/%Y'),
          f'{locale.currency(valor_parcela, grouping=True)}')


print(
    f'Você pegou {locale.currency(valor_total, grouping=True)} para pagar \n'
    f'em {delta_anos.years} anos. '
    f'O numero de parcelas são: {numero_parcelas} \n'
    f'Valor de cada parcela é: {locale.currency(valor_parcela, grouping=True)}'
)
