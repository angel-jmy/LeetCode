# Write your MySQL query statement below
-- select distinct l1.num as ConsecutiveNums
-- from Logs as l1, Logs as l2, Logs as l3
-- where l1.id = l2.id - 1 and l1.id = l3.id - 2
-- and 
-- l1.num = l2.num and l1.num = l3.num


with combined as (
    select id, num, 
        lag(num, 1) over (order by id) as back1,
        lag(num, 2) over (order by id) as back2
    from Logs
)

select distinct num as ConsecutiveNums
from combined 
where num = back1 and num = back2