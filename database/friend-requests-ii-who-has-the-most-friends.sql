# Write your MySQL query statement below
with friends1 as (
    select accepter_id as id, count(*) as counts
    from RequestAccepted
    group by id
),

friends2 as (
    select requester_id as id, count(*) as counts
    from RequestAccepted
    group by id
),

friends as (
    select friends1.id, coalesce(friends1.counts, 0) + coalesce(friends2.counts, 0) as num 
    from friends1
    left join friends2
    on friends1.id = friends2.id

    union 

    select friends2.id, coalesce(friends1.counts, 0) + coalesce(friends2.counts, 0) as num 
    from friends1
    right join friends2
    on friends1.id = friends2.id
)

select id, num from friends
where num = (select max(num) from friends)
