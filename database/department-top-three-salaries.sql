# Write your MySQL query statement below
with ranked as (
    select d.name as `Department`, e.name as `Employee`, salary as Salary,
        dense_rank() over (partition by d.id order by salary desc) as rnk
    from Department d join Employee e
    on d.id = e.departmentId
)

select `Department`, `Employee`, Salary
from ranked
where rnk <= 3