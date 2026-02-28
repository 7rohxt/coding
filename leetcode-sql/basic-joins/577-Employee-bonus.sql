select e.name, b.bonus
from Employee e
left join Bonus b 
    on e.empId = b.empID
where b.bonus < 1000  or b.bonus is null