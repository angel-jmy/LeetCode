-- Write your PostgreSQL query statement below
with lags as (
    select id, num, coalesce(lag(num) over (order by id), 0) as prev
    from Logs
),

flags as (
    select id, num, 
     case when num = prev then 0 else 1 end as flag
    from lags
),

sums as (
    select id, num, sum(flag) over (order by id) as grp
    from flags
),

grouped as (
    select grp, count(*) as cnt
    from sums
    group by grp
    having count(*) >= 3
)

select distinct s.num as ConsecutiveNums
from sums s
join grouped g
on s.grp = g.grp;