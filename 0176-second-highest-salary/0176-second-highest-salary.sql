# # Write your MySQL query statement below
# SELECT salary as SecondHighestSalary 
# FROM Employee
# ORDER BY Salary DESC
# LIMIT 1 OFFSET 1

SELECT (SELECT DISTINCT salary
FROM  Employee
ORDER BY salary DESC
LIMIT 1 OFFSET 1) AS SecondHighestSalary