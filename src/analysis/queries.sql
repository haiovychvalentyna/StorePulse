-- ========================================================
-- ФІНАЛЬНІ АНАЛІТИЧНІ ЗАПИТИ ДЛЯ ПРОЕКТУ STOREPULSE
-- ========================================================

-- 1. Загальний виторг магазину (Total Revenue)
SELECT SUM(total_amount) AS total_revenue 
FROM Orders;

-- 2. Кількість замовлень та середній чек (AOV)
SELECT 
    COUNT(order_id) AS total_orders,
    AVG(total_amount) AS average_order_value
FROM Orders;

-- 3. Топ-5 найпопулярніших товарів за кількістю продажів
SELECT 
    p.product_name, 
    p.category, 
    SUM(oi.quantity) AS total_quantity_sold
FROM Order_Items oi
JOIN Products p ON oi.product_id = p.product_id
GROUP BY p.product_id
ORDER BY total_quantity_sold DESC
LIMIT 5;

-- 4. Розподіл виторгу та замовлень за містами покупців
SELECT 
    c.city, 
    COUNT(o.order_id) AS total_orders,
    SUM(o.total_amount) AS revenue_by_city
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id
GROUP BY c.city
ORDER BY revenue_by_city DESC;

-- 5. Щомісячна динаміка продажів магазину
SELECT 
    DATE_FORMAT(order_date, '%Y-%m') AS sales_month,
    COUNT(order_id) AS total_orders,
    SUM(total_amount) AS monthly_revenue
FROM Orders
GROUP BY sales_month
ORDER BY sales_month ASC;
