# Write your MySQL query statement below
with ranked as (
    select departmentId, name, salary,
            dense_rank() over (partition by departmentId order by salary desc) as rnk
    from Employee
)

select d.name as `Department`, r.name as `Employee`, r.salary as `Salary`
from ranked r
join Department d
on r.departmentId = d.id
where rnk = 1