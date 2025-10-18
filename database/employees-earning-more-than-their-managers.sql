# Write your MySQL query statement below
-- select e.name as Employee from Employee as e, Employee as m
-- where e.managerId = m.id
-- and
-- e.salary > m.salary


select e.name as `Employee`
from Employee e
join Employee m
on e.managerId = m.id
where e.salary > m.salary