select euni.unique_id, e.name 
from Employees e
left join EmployeeUNI euni
    on e.id = euni.id