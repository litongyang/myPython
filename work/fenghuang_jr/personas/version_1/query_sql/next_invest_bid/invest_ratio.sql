set hive.exec.compress.output=false;
insert overwrite local directory '/root/personas_fengjr/data/next_invest_bid' row format delimited fields terminated by '\t'

select
  user_id,
  concat_ws(',', collect_list(cast(t.deadline as string))) as deadline_list,
  concat_ws(',', collect_list(cast(t.rate as string))) as rate_list
from
(
  select
    user_id,
    invest_tm,
    (loan_days + loan_months*30 + loan_years*365) as deadline,
    loan_rate_ori as rate
  from
    dwi.dwi_ordr_invest_full
  where
    dt = '${dt}'
    and invest_status in(
      'FROZEN',
      'FINISHED',
      'SETTLED',
      'CLEARED',
      'OVERDUE',
      'BREACH'
  )
order by
  invest_tm
)t
group by
  user_id