select s.first_name,
    s.last_name,
    sub.name as "subject",
    t.first_name as "teacher_first_name",
    t.last_name as "teacher_last_name",
    sum (r.score) as "total"
from results r
    join students s on r.student_id = s.id
    join subjects sub on r.subject_id = sub.id
    join teachers t on r.teacher_id = t.id
where sub.name = "Music"
group by s.first_name,
    s.last_name
having total < 25
order by s.last_name,
    s.first_name;