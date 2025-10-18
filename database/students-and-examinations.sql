# Write your MySQL query statement below
select s.student_id, 
student_name, 
sub.subject_name, 
sum(e.subject_name is not null) as attended_exams 
from Students s
cross join Subjects sub
left join Examinations e
on s.student_id = e.student_id and sub.subject_name = e.subject_name
group by s.student_id, sub.subject_name
order by s.student_id, sub.subject_name
