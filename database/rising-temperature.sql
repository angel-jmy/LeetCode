# Write your MySQL query statement below
with combined as (
    select w.id, w.recordDate, w.temperature, p.temperature as p_temp
    from Weather w join Weather p
    on w.recordDate = p.recordDate + interval 1 day
)

select id from combined
where temperature > p_temp