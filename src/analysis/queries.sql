-- =====================================================================
-- АНАЛІТИЧНІ SQL-ЗАПИТИ ДЛЯ ПРОЄКТУ STOREPULSE
-- =====================================================================

-- 1. Загальний виторг магазину (Total Revenue)
-- Показує суму брудного прибутку від усіх замовлень
SELECT SUM(total_amount) AS total_revenue 
FROM Orders;


-- 2. Кількість замовлень та середній чек (AOV - Average Order Value)
-- Базова бізнес-метрика для оцінки середніх витрат одного покупця
SELECT 
    COUNT(order_id) AS total_orders,
    AVG(total_amount) AS average_order_value
FROM Orders;


-- 3. Топ-5 найпопулярніших товарів за кількістю продажів
-- Допомагає визначити головні бестселери магазину
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
-- Географічний аналіз продажів для маркетингу
SELECT 
    c.city, 
    COUNT(o.order_id) AS total_orders,
    SUM(o.total_amount) AS revenue_by_city
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id
GROUP BY c.city
ORDER BY revenue_by_city DESC;


-- 5. Щомісячна динаміка продажів магазину
-- Аналіз трендів та зростання компанії по місяцях
SELECT 
    DATE_FORMAT(order_date, '%Y-%m') AS sales_month,
    COUNT(order_id) AS total_orders,
    SUM(total_amount) AS monthly_revenue
FROM Orders
GROUP BY sales_month
ORDER BY sales_month ASC;


-- 6. Топ-5 найактивніших клієнтів (VIP-покупці за сумою витрат)
-- Визначає покупців, які приносять магазину найбільше грошей
SELECT 
    c.full_name,
    c.city,
    COUNT(o.order_id) AS orders_count,
    SUM(o.total_amount) AS total_spent
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_id
ORDER BY total_spent DESC
LIMIT 5;


-- 7. Середня кількість товарів в одному чеку (Basket Size)
-- Показує, скільки одиниць товару клієнти зазвичай кладуть у кошик
SELECT AVG(quantity_per_order) AS average_basket_size
FROM (
    SELECT order_id, SUM(quantity) AS quantity_per_order
    FROM Order_Items
    GROUP BY order_id
) AS order_counts;


-- 8. Популярність категорій товарів за кількістю проданих одиниць
-- Демонструє, який відділ магазину є лідером за обсягами продажів
SELECT 
    p.category,
    SUM(oi.quantity) AS total_units_sold,
    COUNT(DISTINCT oi.order_id) AS unique_orders_count
FROM Order_Items oi
JOIN Products p ON oi.product_id = p.product_id
GROUP BY p.category
ORDER BY total_units_sold DESC;


-- 9. Клієнти, які зареєструвалися, але ще не зробили жодного замовлення
-- Аналіз пасивної аудиторії для подальшої роботи маркетологів
SELECT c.full_name, c.city, c.registration_date
FROM Customers c
LEFT JOIN Orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;


-- 10. Аналіз продажів за днями тижня (Сезонність активності)
-- Показує, у які дні тижня (від неділі=1 до суботи=7) клієнти купують найактивніше
SELECT 
    DAYNAME(order_date) AS day_of_week,
    COUNT(order_id) AS total_orders,
    SUM(total_amount) AS revenue
FROM Orders
GROUP BY day_of_week
ORDER BY FIELD(day_of_week, 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday');
