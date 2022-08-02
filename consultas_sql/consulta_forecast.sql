-- Uma consulta que tenha:
-- (tb_orders): data_pedido, status do pedido, 
-- (tb_orders_items) id_produto, preço, frete,
-- (tb_products)categoria do produto, qtd_foto_do_produto, 
-- (tb_customers) cidade do comprador,
-- (tb_sellers) cidade do vendedor

WITH tb_orders_join AS (
    SELECT
        *

    FROM tb_order_items AS t1
    LEFT JOIN tb_orders AS t2
        ON t1.order_id =  t2.order_id

    WHERE t2.order_status != "canceled"
),

tb_orders_join_product_city AS (
    SELECT 
        t1.order_purchase_timestamp AS date_time_purchase,
        t4.seller_id,
        t3.customer_id,
        t1.order_id,
        t1.order_status,
        t1.order_item_id,
        t1.product_id,
        t2.product_category_name,
        t1.price,
        t1.freight_value,        
        t3.customer_city,
        t4.seller_city
        
    FROM tb_orders_join AS t1
    LEFT JOIN tb_products AS t2
        ON t1.product_id = t2.product_id
    
    LEFT JOIN tb_customers AS t3
        ON t1.customer_id = t3.customer_id

    LEFT JOIN tb_sellers AS t4
        ON t1.seller_id = t4.seller_id

    ORDER BY date_time_purchase, t1.order_id, t1.order_item_id

)

SELECT
    *
FROM tb_orders_join_product_city;
