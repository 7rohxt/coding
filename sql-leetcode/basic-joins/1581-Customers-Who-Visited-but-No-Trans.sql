select v.customer_id, count(v.visit_id)-count(t.transaction_id) as count_no_trans
from Visits v
left join Transactions t
    on v.visit_id = t.visit_id
group by v.customer_id
having count_no_trans > 0