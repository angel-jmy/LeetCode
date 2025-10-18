# Write your MySQL query statement below
#### Grouping 1

-- WITH Valid AS (
--   SELECT *, 
--          id - ROW_NUMBER() OVER (ORDER BY id) AS grp
--   FROM Stadium
--   WHERE people >= 100
-- ),
-- Grouped AS (
--   SELECT grp
--   FROM Valid
--   GROUP BY grp
--   HAVING COUNT(*) >= 3
-- )
-- SELECT v.id, v.visit_date, v.people
-- FROM Valid v
-- JOIN Grouped g ON v.grp = g.grp
-- ORDER BY v.visit_date;

#### Grouping 2
with cuts as (
    select *,
        sum(case when people < 100 then 1 else 0 end) 
        over (order by id
            rows between unbounded preceding and current row) as grp
    from Stadium
),

groupings as (
    select grp, count(*) as streaks
    from cuts
    where people >= 100
    group by grp
    having count(*) >= 3
)

select id, visit_date, people
from cuts c
join groupings g
on c.grp = g.grp
where people >= 100



-- ##### Lags and Leads
-- SELECT ID
--     , visit_date
--     , people
-- FROM (
--     SELECT ID
--         , visit_date
--         , people
--         , LEAD(people, 1) OVER (ORDER BY id) nxt
--         , LEAD(people, 2) OVER (ORDER BY id) nxt2
--         , LAG(people, 1) OVER (ORDER BY id) pre
--         , LAG(people, 2) OVER (ORDER BY id) pre2
--     FROM Stadium
-- ) cte 
-- WHERE (cte.people >= 100 AND cte.nxt >= 100 AND cte.nxt2 >= 100) 
--     OR (cte.people >= 100 AND cte.nxt >= 100 AND cte.pre >= 100)  
--     OR (cte.people >= 100 AND cte.pre >= 100 AND cte.pre2 >= 100) 
