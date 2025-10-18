# Write your MySQL query statement below
select class from (
    select class, count(*) as students
    from Courses
    group by class
    having students >= 5
) as counts
