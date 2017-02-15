set hive.exec.compress.output=false;
insert overwrite local directory '/root/personas_fengjr/data/invest_var' row format delimited fields terminated by '\t'
select
  user_id,
  stddev(loan_rate_ori) as rate_var
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
group by
  user_id