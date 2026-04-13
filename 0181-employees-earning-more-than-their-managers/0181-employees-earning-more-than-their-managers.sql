# Write your MySQL query statement below


SELECT p.name as Employee from Employee p join  Employee m where p.salary > m.salary and p.managerId = m.id;  