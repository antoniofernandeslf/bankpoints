import apache_beam as beam

def calculate_points(element):
    custumer_id, first_name, last_name, relationship_id, card_type, max_limit, spent, card_withdraw, payment_cleared, payment_date = element.split(',')

    spent = int(spent)
    payment_cleared = int(payment_cleared)
    max_limit = int(max_limit)

    key_name = custumer_id + ',' + first_name + ',' + last_name
    defaulter_pts = 0

#Verifica se valor pago é menor de 70%
    if payment_cleared < (spent * 0.7):
        defaulter_pts += 1

#Verifica se o gasto é igual ao limite, e se a fatura foi totalmente paga
    if (spent == max_limit) and (payment_cleared < spent):
        defaulter_pts += 1

#Verifica se atende as duas condições acima
    if (spent == max_limit) and (payment_cleared < (spent * 0.7)):
        defaulter_pts += 1

    return key_name, defaulter_pts


p = beam.Pipeline()

defaulter = (
    p
#Leitura dos dados para a collection
    | 'Read data' >> beam.io.ReadFromText('datasets/cards.txt', skip_header_lines=1)
#retorna "lista" de clientes e seus pontos no por mês
    | 'Calculate points' >> beam.Map(calculate_points)
#Agrupa todos os clientes com a mesma chave(criada na função calculate) somando os pontos
    | 'Combine poits' >> beam.CombinePerKey(sum)
#Filtra apenas os que possuem pontos > 0
    | 'Filter defaulters' >> beam.Filter(lambda element: element[1] > 0)
#Salva o resultado
    | 'Write credit card data' >> beam.io.WriteToText("output/cc_skippers")
)
p.run()
