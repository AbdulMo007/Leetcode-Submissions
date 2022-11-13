SELECT name as Customers
FROM Customers
WHERE id NOT IN
(select customerid from customers
inner join orders
on customers.id=orders.customerId);