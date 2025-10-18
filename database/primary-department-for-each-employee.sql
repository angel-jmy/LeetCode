# Write your MySQL query statement below
select employee_id, department_id
from Employee e1
where primary_flag = 'Y'
or (select count(*) from Employee e2
    where e2.employee_id = e1.employee_id) = 1
    