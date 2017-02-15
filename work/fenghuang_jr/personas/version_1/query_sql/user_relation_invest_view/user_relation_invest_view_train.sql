set hive.exec.compress.output=false;
insert overwrite local directory '/root/personas_fengjr/data/user_relation_invest_view' row format delimited fields terminated by '\t'
select
  a.user_id,
  b.deadline_type,
  b.bid_type,
  b.veiw_bid_cnt,
  case when c.invest_bid_cnt is NULL then 0
  else c.invest_bid_cnt end as invest_bid_cnt,
  case when c.invest_bid_cnt is NULL then 0
  else 1 end as is_invest
from
 dim.dim_user_base as a
join
(
  select
      user_id,
      deadline_type,
      bid_type,
      count(loan_id) as veiw_bid_cnt
  from
  (
  select
     user_id,
     loan_id,
     loan_years*365+loan_months*30+loan_days as deadline_days,
     case when (loan_days + loan_months*30 + loan_years*365) <60 then 'short'
           when (loan_days + loan_months*30 + loan_years*365) >=60 and (loan_days + loan_months*30 + loan_years*365) <=180 then 'between'
           else 'long' end as deadline_type,
     case when cast(loan_rate*10000 as float)<500 then 'low'
           when cast(loan_rate*10000 as float) >=500 and cast(loan_rate*10000 as float)<=650 then 'mid'
           else 'high' end as bid_type
  from
    dwi.dwi_flow_online_log
  where
    dt >= '${before}'
    and loan_id <>''
  )t
  group by user_id,deadline_type,bid_type
)as b
on
 a.user_id = b.user_id
left outer join
(
  select
    user_id,
    deadline_type,
    bid_type,
    count(loan_id) as invest_bid_cnt
  from
  (
    select
      user_id,
      loan_id,
      case when (loan_days + loan_months*30 + loan_years*365) <60 then 'short'
           when (loan_days + loan_months*30 + loan_years*365) >=60 and (loan_days + loan_months*30 + loan_years*365) <=180 then 'between'
           else 'long' end as deadline_type,
      case when cast(loan_rate_ori as float)<500 then 'low'
           when cast(loan_rate_ori as float) >=500 and cast(loan_rate_ori as float)<=650 then 'mid'
           else 'high' end as bid_type
    from
      dwi.dwi_ordr_invest_full
    where
      dt = '${dt}'
      and substr(invest_tm,1,10) >='${before}'
      and invest_status in(
      'FROZEN',
      'FINISHED',
      'SETTLED',
      'CLEARED',
      'OVERDUE',
      'BREACH'
      )
  )t
  group by
    user_id, deadline_type, bid_type
)as c
on
  a.user_id = c.user_id
  and b.deadline_type = c.deadline_type
  and b.bid_type = c.bid_type
