# Olist
Repositório com projetos aplicados em cima da base de dados da olist.

## Sumário
* [Motivação](#motivação);
* [Estrutura do banco de dados](#estrutura-do-banco-de-dados);
* [Ferramentas utilizadas](#ferramentas-utilizadas);
* [Projetos](#projetos-ideias).

## Motivação
Com o desenvolvimento desse projeto, espera-se que seja possível simular demandas existentes do negócio no setor de e-commerce.

## Estrutura do banco de dados
O [esquema](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) do banco de dados que será utilizado nos projetos está ilustrado abaixo:  

![esquema banco de dados](img/HRhd2Y0.png)

O arquivo .db foi preparado pelo [Téo Calvo](https://github.com/TeoCalvo) e pode ser baixado nesse [repositório](https://github.com/TeoCalvo/teoSQL-V2).

## Ferramentas utilizadas
Para reproduzir esse projeto, basta dar o comando `pip install requirements.txt`, mas seguem as principais tecnologias utilizadas:
* SQL (SQLite);
* Python;
* PySpark (rodando localmente);

## Projetos propostos (em desenvolvimento)
* [Previsão de vendas (Forecasting)](forecasting/);
* Segmentação de clintes;
* Atraso no pedido;
* Review.