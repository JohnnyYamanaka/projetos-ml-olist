# Forecasting Olist
## Sumário
  - [Sumário](#sumário)
  - [Escopo do Projeto](#escopo-do-projeto)
  - [Motivação](#motivação)
  - [Os Dados](#os-dados)
  - [Etapas do Projeto](#etapas-do-projeto)

## Escopo do Projeto
Desenvolver um modelo capaz de realizar forecasting (em $ ou em qtd) para uma determinada categoria de produtos que ainda será definido.

## Motivação
Conhecer melhor o comportamento de vendas do negócio pode garantir que seja tomada decisões mais consistentes efetivos, como preparar o seu estoque para uma determinada época do ano, aumentar ou diminuir o preço de venda, ter previsibilidade de receita e assim por diante.  

## Os Dados
Os dados foram retirados do banco de dados da Olist, onde foi realizado uma [consulta](../consultas_sql/consulta_forecast.sql) para obter uma única tabela contendo informações como: data e hora da realização da compra, o status do pedido, quantidade de itens no pedido, categoria do produto, preço e frete e etc.  
A consulta pode ser incrementada se durante a exploração dos dados achar que pode contribuir para o desenvolvimento da solução.

## Etapas do Projeto
O projeto será desenvolvido utilizando o padrão CRISP-DM.
