# Write your MySQL query statement below
-- with filtered as (
--     select e.managerId from Employee as e 
--     join Employee as m
--     on e.managerId = m.id
-- )
-- select name from
-- (
--     select f.managerId as id, count(*) as counts
--     from filtered as f
--     group by id
--     having counts >= 5
-- ) as counted
-- join Employee as e
-- on counted.id = e.id


with ids as (
    select managerId, count(*) as counts
    from Employee
    group by managerId
    having counts >= 5
)

select name 
from Employee e
join ids i 
on e.id = i.managerId