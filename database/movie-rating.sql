# Write your MySQL query statement below
with num_rating as (
    select user_id, count(movie_id) as counts 
    from MovieRating
    group by user_id
),

max_user as (
    select name
    from Users u
    join num_rating n
    on u.user_id = n.user_id
    where counts = (select max(counts) from num_rating)
    order by name
    limit 1
),
avg_rating as (
    select movie_id, avg(rating) as avg_rate 
    from MovieRating
    where created_at between '2020-02-01' and '2020-02-29'
    group by movie_id
),

high_movie as (
    select title
    from Movies m
    join avg_rating r
    on m.movie_id = r.movie_id
    where avg_rate = (select max(avg_rate) from avg_rating)
    order by title
    limit 1
)

select name as results
from max_user

union all

select title as results
from high_movie
