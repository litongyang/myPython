use crm_v2;
insert overwrite local directory '/data/ml/tongyang/test/data/next_invest_bid'

select
    a.user_id,
    concat_ws(',', collect_list(cast(a.deadline as string))),
    concat_ws(',', collect_list(cast(a.rate as string)))
from
(
  select
     inv.USERID as user_id,
     inv.SUBMITTIME as submit_time,
     (lo.days + lo.months*30 +lo.years*365) as deadline,
     lo.rate as rate
  from
	TB_LOANREQUEST_PRIVILEGE AS lp,
	TB_LOAN AS lo,
	TB_INVEST AS inv
	WHERE
		lo.REQUEST_ID = lp.REQUEST_ID
		AND lo.ID = inv.LOANID
		AND inv.STATUS IN (
		'FROZEN',
		'FINISHED',
		'SETTLED',
		'CLEARED',
		'OVERDUE',
		'BREACH',
		'TURNOUT')
    order by submit_time
) a
group by  a.user_id