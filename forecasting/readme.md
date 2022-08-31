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
A execução desse projeto seguiu a metodologia CRISP-DM:

* [Entendimento dos dados](#entendimento-dos-dados);
* [Preparação dos dados para modelagem](#preparação-dos-dados);
* Modelagem;
* Avaliação do desempenho.
  
## Entendimento dos Dados
O dataset possui dados de vendas de setembro de 2016 à setembro de 2018, porém durante a exploração dos dados, foi observado que que apesar do dataset possuir informações de 2 anos de venda, o primeiro ano (2016) precisou ser descartada, pois não havia dados suficientes e não agregaria na modelagem.  
No mais, foram verificados as principais estatísticas sobre cada feature para tentar identificar padrões e/ou desvios. Pode-se verificar que houve um pico de vendas no final de novembro 2017 por conta da black friday deste ano, ligando o alerta para como lidar com eventuais picos gerados por dias/eventos festivos.  
Alguns dos principais insights da análise foram:
* A maioria dos pedidos vem predominantemente do estado de São Paulo;
* A maior parte dos vendedores se encontram na região sudeste, também com predominância do estado de São Paulo;
* Os clientes tendem a realizar os pedidos durante a semana (de segunda à sexta);
* Existe uma tendência positiva nas vendas - ao longo da série o faturamento vai crescendo, mesmo que seja lentamente;
* A black friday de 2017 impactou positivamente o negócio - além do recorde de vendas do período observado, a partir deste ponto o faturamento passou a ficar acima da média de faturamento do período (mesmo com a queda do final do ano).

## Preparação dos dados
Antes de realizar a modelagem, foi acrescentado mais algumas features através da classe [`FeatureEngineering`](helpers/feature_engineering.py), que podem ser interessante para o nosso problema. Entre eles:
* `is_holiday`: indica se naquela data foi comemorado algum feriado;
* `is_commercial_day`: indica se naquela data existiu alguma data relevante para o varejo, como dia dos pais, blackfriday, dia dos namorados e etc;
* `day_of_week`: indica o dia da semana (0 para segunda feira e 7 para domingo);
* `day_of_month`: indica o dia do mês;
* `day_of_year`: indica o dia do ano;
* `moving_average`: as médias móveis das vendas (período de 7, 14 e 21 dias);
* `diff_yesterday_sales`: a diferença de venda em relação ao dia anterior;
* `lag_sales`: indica o número de venda passada de um determinado período. Foi testado o período de 1, 7, 14, 21 e 28 dias.

A avaliação da utilizade das features será realizada na etapa de modelagem.
