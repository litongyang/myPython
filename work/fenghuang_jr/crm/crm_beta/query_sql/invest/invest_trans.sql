use crm_v2;
insert overwrite table crm_invest_status
select
	user_id,
	all_count,
	no_debt_swap_cnt,
	debt_swap_cnt,
	case when is_new_user = 0 then no_debt_swap_cnt else no_debt_swap_cnt-1 end  as no_debtSwap_newUser_cnt,
	all_amount,
	no_debt_swap_amount,
	debt_swap_amount,
	brushstroke_amount_max,
	brushstroke_amount_min,
	new_user_amount,
	no_new_user_amount,
	first_time,
	lastest_time,
	is_new_user,
	new_user_submit_time,
	pc_invest_cnt,
	app_invest_cnt,
	h5_invest_cnt,
	other_channel_cnt,
	case when is_new_user = 1 then round((no_debt_swap_cnt - 1) / all_count,2) else round(no_debt_swap_cnt / all_count,2) end  as no_debtSwap_newUser_cnt_ratio,
	round(no_debt_swap_cnt / all_count,2) as  no_debt_swap_cnt_ratio,
	round(debt_swap_cnt / all_count,2) as debt_swap_cnt_ratio,
	round((no_debt_swap_amount - new_user_amount) / all_amount,2) as no_debt_swap_amount_ratio,
	round(debt_swap_amount / all_amount,2) as debt_swap_amount_ratio,
	round(new_user_amount / all_amount, 2) as new_amount_ratio,
	round(pc_invest_cnt / all_count, 2) as pc_invest_cnt_ratio,
	round(app_invest_cnt / all_count, 2) as app_invest_cnt_ratio,
	round(h5_invest_cnt / all_count, 2) as h5_invest_cnt_ratio,
	first_new_days,
	first_new_title,
	last_new_amount
from
(
	select
		i.USERID as user_id,
		count(i.USERID) AS all_count,
		sum(case when i.CREDITASSIGNID = 'null' then 1 else 0 end) as no_debt_swap_cnt,
		sum(case when i.CREDITASSIGNID = 'null' then 0 else 1 end) as debt_swap_cnt,
		(if(sum(case when i.CREDITASSIGNID = 'null' then (case when i.ORIGINALAMOUNT is null then i.amount else i.ORIGINALAMOUNT end) else 0 end) is not null, sum(case when i.CREDITASSIGNID = 'null' then (case when i.ORIGINALAMOUNT is null then i.amount else i.ORIGINALAMOUNT end) else 0 end), 0) + if(re.debt_swap_amount is not null,re.debt_swap_amount,0)) as all_amount,
		 sum(case when i.CREDITASSIGNID = 'null' then (case when i.ORIGINALAMOUNT is null then i.amount else i.ORIGINALAMOUNT end) else 0 end) as no_debt_swap_amount,
		 re.debt_swap_amount as debt_swap_amount,
		substr(min(case when i.CREDITASSIGNID = 'null' then i.SUBMITTIME else '3000-01-01 ' end),1,10) AS first_time,
		substr(max(case when i.CREDITASSIGNID = 'null' then i.SUBMITTIME else '0000-00-00 00:00:00.0' end),1,10) AS lastest_time,
		-- DATE_FORMAT(min(case when i.CREDITASSIGNID is null then i.SUBMITTIME else '3000-01-01' end),'%Y-%m-%d') AS first_time,
		-- DATE_FORMAT(max( case when i.CREDITASSIGNID is null then i.SUBMITTIME else '0' end),'%Y-%m-%d') AS lastest_time,
		max(case when i.CREDITASSIGNID = 'null' then (case when i.ORIGINALAMOUNT is null then i.amount else i.ORIGINALAMOUNT end) else 0 end)  AS brushstroke_amount_max,
		min(case when i.CREDITASSIGNID = 'null' then (case when i.ORIGINALAMOUNT is null then i.amount else i.ORIGINALAMOUNT end) else null end) AS brushstroke_amount_min,
		case when new.USERID is NULL then 0 else 1 end as is_new_user,
		substr(new.submit_time,1,10)as new_user_submit_time,
		-- DATE_FORMAT(new.submit_time,'%Y-%m-%d') as new_user_submit_time,
		case when new.amount is not null then new.amount else 0 end as new_user_amount,
	    sum(case when i.CREDITASSIGNID = 'null' then (case when i.ORIGINALAMOUNT is null then i.amount else i.ORIGINALAMOUNT end) else 0 end) - case when new.amount is null then 0 else new.amount end as no_new_user_amount,
		sum(case when i.SOURCE = 'WEB' then 1 else 0 end) as pc_invest_cnt,
		sum(case when i.SOURCE = 'ANDROID'or i.SOURCE = 'IOS' then 1 else 0 end) as app_invest_cnt,
		sum(case when i.SOURCE = 'MOBILEWEB' then 1 else 0 end) as h5_invest_cnt,
		sum(case when i.SOURCE is null then 1 else 0 end) as other_channel_cnt,
		case when new.amount is not null then new.amount else 0 end as last_new_amount,
		new.new_days as first_new_days,
		new.first_new_title as first_new_title
	FROM
		TB_USER AS u
	JOIN
		TB_INVEST AS i
	ON
		u.ID = i.USERID
	LEFT OUTER JOIN
	(
		SELECT
			USER_ID AS user_id,
			SUM(amount) as debt_swap_amount
		FROM
			TB_FUND_RECORD
	    WHERE
	    	type='INVEST' and status='INITIALIZED' and operation='OUT' and realm in ('CREDITASSIGNINVEST')
	    GROUP BY
	    	USER_ID
	) re
	on
		i.USERID = re.user_id
	LEFT OUTER JOIN
		TB_LOAN l
	ON
		i.LOANID = l.ID
	LEFT OUTER JOIN (
		SELECT
			inv.USERID,
			inv.SUBMITTIME AS submit_time,
			inv.DAYS+inv.MONTHS*30+inv.YEARS*365 as new_days,
			case when inv.ORIGINALAMOUNT is null then inv.amount else inv.ORIGINALAMOUNT end  AS amount,
			lo.title as first_new_title
		FROM
			TB_LOANREQUEST_PRIVILEGE AS lp,
			TB_LOAN AS lo,
			TB_INVEST AS inv
		WHERE
			lo.REQUEST_ID = lp.REQUEST_ID
		AND lp.TYPE = 'LOAN_FOR_NEW_USER'
		AND lo.ID = inv.LOANID
		AND inv.CREDITASSIGNID = 'null'
		AND inv.STATUS IN (
			'FROZEN',
			'FINISHED',
			'SETTLED',
			'CLEARED',
			'OVERDUE',
			'BREACH',
			'TURNOUT')
	) AS new
	ON
			i.USERID = new.USERID
	WHERE
		i. STATUS IN (
		'FROZEN',
		'FINISHED',
		'SETTLED',
		'CLEARED',
		'OVERDUE',
		'BREACH',
		'TURNOUT'
	)
	GROUP BY
		i.USERID,re.debt_swap_amount,new.USERID,new.amount, new.new_days,new.first_new_title,new.submit_time
)t
