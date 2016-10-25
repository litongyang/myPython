use crm_v2;
insert overwrite local directory '/data/ml/tongyang/test/data/user_relation_invest'
select
  user_id,
  deadline_type,
  bid_type,
  count(bid_id) as bid_num
from
(
select
     t1.user_id,
     t2.bid_id,
     t2.rate,
     t2.deadline,
     t2.deadline_type,
     t2.bid_type
from
(
  select
     USERID as user_id,
     LOANID as bid_id
  from
  TB_INVEST
  where
    -- AND inv.CREDITASSIGNID = 'null'
        -- USERID = '001CE49D-5D50-4D65-B4AE-AB80812CC739'
    STATUS IN (
    'FROZEN',
    'FINISHED',
    'SETTLED',
    'CLEARED',
    'OVERDUE',
    'BREACH',
    'TURNOUT')
)t1
left outer join
(
  select
    id as bid_id,
    rate,
    (days + months*30 + years*365) as deadline,
    case when (days + months*30 + years*365) <60 then 'short'
         when (days + months*30 + years*365) >=60 and (days + months*30 + years*365) <=180 then 'in'
         else 'long' end as deadline_type,
    case when cast(rate as float)<500 then 'low'
         when cast(rate as float) >=500 and cast(rate as float)<=650 then 'mid'
         else 'high' end as bid_type
  from
    TB_LOAN
)t2
on
  t1.bid_id = t2.bid_id
)t
group by
  user_id,bid_type,deadline_type