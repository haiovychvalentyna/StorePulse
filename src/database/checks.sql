-- 1. Пошук замовлень без реальних клієнтів
SELECT * FROM Orders 
WHERE customer_id NOT IN (SELECT customer_id FROM Customers);

-- 2. Пошук товарів у чеках, яких немає в таблиці Products
SELECT * FROM Order_Items 
WHERE product_id NOT IN (SELECT product_id FROM Products);

-- 3. Перевірка на помилкові суми
SELECT * FROM Orders 
WHERE total_amount <= 0;
