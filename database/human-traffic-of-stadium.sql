# Write your MySQL query statement below
with flags as (
    select id, visit_date, people, 
    case when people < 100 then 1 else 0 end as flag
    from Stadium
),

grps as (
    select id, visit_date, people, 
    sum(flag) over (order by visit_date asc) as grp
    from flags
),

grouped as (
    select grp, count(*) as days
    from grps
    where people >= 100
    group by grp
    having count(*) >= 3
)

select id, visit_date, people
from grps
join grouped
on grps.grp = grouped.grp
where people >= 100