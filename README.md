# Bank
Atividade referente ao curso: Apache Beam | A Hands-On course to Build Big Data Pipelines

Link: https://www.udemy.com/course/apache-beam-a-hands-on-course-to-build-big-data-pipelines/

Nestre projeto é simulado situações que podem ser encontrados em instituições bancárias.




### Problema 1

Sistema de pontos para os clientes de cartão de crédito seguindo as seguintes regras:

- 1+ ponto por pagamento insuficiente, onde pagamento insuficiente é quando o cliente falha ao pagar ao menos 70% da fatura mensal.
- 1+ ponto para o cliente que utilizou 100% de seu limite mas não pagou a fatura inteira.
- 1+ se em algum mês o cliente, simultanêamente, se enquadrar nas duas condições acima. 

Ao final, o total de pontos deve ser exportado em um arquivo.

## Deploy

 - Clone este repositório: $ git clone https://github.com/antoniofernandeslf/bankpoints.git
 - Ative o ambiente virtual: $ source venv/bin/activate
 - Execute o script python: $ python ccskippers.py

