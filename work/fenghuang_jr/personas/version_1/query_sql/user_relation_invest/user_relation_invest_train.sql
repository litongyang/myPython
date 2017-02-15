set hive.exec.compress.output=false;
insert overwrite local directory '/root/personas_fengjr/data/user_relation_invest' row format delimited fields terminated by '\t'
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