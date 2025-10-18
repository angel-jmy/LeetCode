# Write your MySQL query statement below
select e.employee_id from Employees e
left join Employees m
on e.manager_id = m.employee_id
where e.manager_id is not Null and e.salary < 30000 and m.employee_id is Null
order by e.employee_id asc