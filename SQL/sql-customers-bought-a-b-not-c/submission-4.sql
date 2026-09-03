-- Write your query below
SELECT c.customer_id, c.customer_name
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING
    SUM(CASE when o.product_name = 'A' then 1 else 0 end) > 0
    AND SUM(case when o.product_name = 'B' then 1 else 0 end) > 0
    AND SUM(case when o.product_name = 'C'then 1 else 0 end) = 0
ORDER BY c.customer_name;
