-- 用户投资标签信息
select
	i.userid as user_id,
	count(i.userid) as invest_cnt,
	sum(re.amount) as all_amount,
	sum(case when i.CREDITASSIGNID is null then 1 else 0 end) as debt_swap_not_cnt,
	count(*)-sum(case when i.CREDITASSIGNID is null then 1 else 0 end) as debt_swap_cnt,
	sum(case when i.CREDITASSIGNID is null then re.amount else 0 end) as debt_swap_not_amount,
	sum(case when i.CREDITASSIGNID is not null then re.amount else 0 end) as debt_swap_not_amount,
	max(re.amount) as brushstroke_amount_max,
	min(re.amount) as brushstroke_amount_min,
	case when new.USERID is NULL then 0 else 1 end as is_new_user,
	DATE_FORMAT(new.submit_time,'%Y-%m-%d') as new_user_submit_time,
	new.amount as new_user_amount,
	sum(re.amount) - new.amount as not_new_user_amount
	/*
	sum(case
		when i.CREDITASSIGNID is null
		-- then (case when i.ORIGINALAMOUNT is null then i.amount else i.ORIGINALAMOUNT end)
		then sre.AMOUNT
	else
		0 end) as debt_swap_not_amount,

	sum(case
		when i.CREDITASSIGNID is not null
		then (case when i.ORIGINALAMOUNT is null then i.amount else i.ORIGINALAMOUNT end)
	else
		0 end) as debt_swap_amount,

	max(case when i.ORIGINALAMOUNT is null then i.amount else i.ORIGINALAMOUNT end) AS brushstroke_amount_max,
	min(case when i.ORIGINALAMOUNT is null then i.amount else i.ORIGINALAMOUNT end) AS brushstroke_amount_min,
	case when new.USERID is NULL then 0 else 1 end as is_new_user,
	DATE_FORMAT(new.submit_time,'%Y-%m-%d') as new_user_submit_time,
	new.amount as new_user_amount,
	sum(case when i.ORIGINALAMOUNT is null then i.amount else i.ORIGINALAMOUNT end) - new.amount as not_new_user_amount
	*/

from
	TB_USER u
join
	TB_INVEST i
on
	u.id = i.userid
join
	TB_FUND_RECORD re
on
	i.ID = re.ENTITYID
-- new user
left outer join
(
	select
		inv.userid,
		inv.SUBMITTIME as submit_time,
		case when inv.ORIGINALAMOUNT is null then inv.amount else inv.ORIGINALAMOUNT end  as amount
	from
		TB_LOANREQUEST_PRIVILEGE lp
	join
		TB_LOAN lo
	on
		lp.REQUEST_ID = lo.REQUEST_ID
	join
		TB_INVEST inv
	on
		lo.ID = inv.LOANID
	where
		lp.TYPE = 'LOAN_FOR_NEW_USER'
		and inv.STATUS IN (
	        'FROZEN',
	        'FINISHED',
	        'SETTLED',
	        'CLEARED',
	        'OVERDUE',
	        'BREACH',
	        'TURNOUT')
) new
on
	i.userid = new.userid
where
	i. STATUS IN (
		'FROZEN',
		'FINISHED',
		'SETTLED',
		'CLEARED',
		'OVERDUE',
		'BREACH',
		'TURNOUT')
group by
	i.userid
LIMIT 10
