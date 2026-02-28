select w2.id
from Weather w1
join Weather w2
    on w1.recordDate = w2.recordDate - interval 1 day
where w2.temperature > w1.temperature