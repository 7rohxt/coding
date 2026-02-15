select s.user_id, round(ifnull(sum(action='confirmed')/count(c.user_id),0),2) confirmation_rate
from Signups s
left join Confirmations c
    on s.user_id = c.user_id
group by s.user_id