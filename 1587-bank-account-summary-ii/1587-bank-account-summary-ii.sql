# Write your MySQL query statement below
SELECT name, SUM(amount) AS balance
FROM Transactions
INNER JOIN Users 
    ON Users.account = Transactions.account
GROUP BY Users.account
HAVING balance > 10000
