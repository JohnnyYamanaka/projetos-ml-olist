-- Quantas vendas foram possui a base de dados?
SELECT 
    COUNT(*) AS qtd_vendas
FROM tb_orders;

-- Quantos vendedores a base possui?
SELECT
    COUNT(DISTINCT(t1.seller_id)) AS qtd_vendedores
FROM tb_order_items AS t1;

-- Qual é o período de transações?
-- considere a data de emissão do pedido
SELECT 
    MIN(t1.order_purchase_timestamp) AS primeira_data,
    MAX(t1.order_purchase_timestamp) AS ultima_data

FROM tb_orders AS t1;

-- Quais são os 5 maiores pedidos? 
-- Considere somente os pedidos já entregue
SELECT
    t1.order_id,
    SUM(t1.price + t1.freight_value) AS valor_total


FROM tb_order_items AS t1
LEFT JOIN tb_orders AS t2
    ON t1.order_id = t2.order_id

WHERE t2.order_status = 'delivered'

GROUP BY t1.order_id
ORDER BY valor_total DESC
LIMIT 5;