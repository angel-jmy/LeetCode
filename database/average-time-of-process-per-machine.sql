# Write your MySQL query statement below
-- with times as (
--     select machine_id, process_id, max(`timestamp`) - min(`timestamp`) as process_time
--     from Activity
--     group by machine_id, process_id
-- )

-- select machine_id, round(avg(process_time), 3) as processing_time
-- from times
-- group by machine_id


-- SELECT
-- machine_id,
-- ROUND(
-- AVG(CASE WHEN activity_type = 'end' THEN `timestamp` END) -
-- AVG(CASE WHEN activity_type = 'start' THEN `timestamp` END), 3
-- ) AS processing_time
-- FROM
-- activity
-- GROUP BY machine_id;


with combined as (
    select a1.machine_id, a1.process_id, a2.`timestamp` - a1.`timestamp` as process_time
    from Activity a1
    join Activity a2
    on a1.machine_id = a2.machine_id and a1.process_id = a2.process_id
    and a1.activity_type = 'start' and a2.activity_type = 'end'
)

select machine_id, round(avg(process_time), 3) as processing_time
from combined
group by machine_id