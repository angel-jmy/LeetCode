-- Write your PostgreSQL query statement below
with flagged as (
    select id, visit_date, people, 
     case when people < 100 then 1 else 0 end as flag
    from Stadium
),

separated as (
    select id, visit_date, people,
     sum(flag) over (order by visit_date asc rows between unbounded preceding and current row) as grp
    from flagged
),

grouped as (
    select grp, count(*) as cnt
    from separated
    where people >= 100
    group by grp
)

select s.id, s.visit_date, s.people
from separated s
join grouped g
on s.grp = g.grp
where g.cnt >= 3 and s.people >= 100;