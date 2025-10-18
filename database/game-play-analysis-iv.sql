# Write your MySQL query statement below
with firstday as (
    select player_id, min(event_date) as mindate
    from Activity
    group by player_id
),
secondday as (
    select f.player_id, date_add(f.mindate, interval 1 day) as secdate
    from firstday f join Activity a
    on date_add(f.mindate, interval 1 day) = a.event_date
    and f.player_id = a.player_id
)

select 
round((
    select count(distinct player_id) from secondday
) / 
(
    select count(distinct player_id) from Activity
), 2) as fraction
























-- with secondday as (
--     select player_id, date_add(min(event_date), interval 1 day) as second_date
--     from Activity
--     group by player_id
-- ),

-- inact as (
--     select Activity.player_id as player_id
--     from Activity, secondday
--     where Activity.player_id = secondday.player_id
--     and Activity.event_date = secondday.second_date
-- )


-- select round((select count(player_id) from inact) / (select count(player_id) from secondday), 2) as fraction