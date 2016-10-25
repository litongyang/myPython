select
	u.id as user_id,
	a.INVEST_ID,
	'p2p' as category,
	DATE_FORMAT(i.SUBMITTIME,'%Y-%m-%d') as submit_time,
	a.due_date as due_date,
	CASE when i.ORIGINALAMOUNT is null then i.amount else i.ORIGINALAMOUNT end as amount,
	a.interest_amount+CASE when i.ORIGINALAMOUNT is null then i.amount else i.ORIGINALAMOUNT end as due_amount
from
TB_INVEST as i,TB_USER as u,
(
	select
		tmp.INVEST_ID,
		case when tmp.REPAYDATE is null then tmp.DUEDATE else DATE_FORMAT(tmp.REPAYDATE,'%Y-%m-%d') end as due_date,
		sum(tmp.AMOUNTINTEREST) as interest_amount
	from
	(
		select
			a.INVEST_ID,
			a.DUEDATE,a.REPAYDATE,
			case when a.REPAYAMOUNT is null then a.AMOUNTINTEREST else a.REPAYAMOUNT-a.AMOUNTPRINCIPAL end as AMOUNTINTEREST
		from
		(
			select
				a.INVEST_ID,
				a.DUEDATE,
				a.REPAYDATE,
				a.REPAYAMOUNT,
				a.AMOUNTPRINCIPAL,
				a.AMOUNTINTEREST
			from
				TB_INVEST_REPAYMENT as a
			where a.STATUS <> 'DEPRECATED' and a.STATUS <> 'COLLECTED'
			order by a.CURRENTPERIOD desc
		) as a
	) as tmp
group by tmp.INVEST_ID

union ALL

select
	a.INVEST_ID,null,null
from
(
	select
		a.INVEST_ID,a.DUEDATE,a.REPAYDATE,a.AMOUNTINTEREST,a.STATUS
	from
		TB_INVEST_REPAYMENT as a
	where a.STATUS = 'DEPRECATED' and a.CURRENTPERIOD=1
) as a

union ALL

select
	i.id,null,null
from
	TB_INVEST as i,
	TB_LOAN as l
where
	i.LOANID=l.id
	and i.status='FROZEN'
	and l.TIMESETTLED is null
) as a
where  i.CREDITASSIGNID IS NULL
AND i. STATUS IN (
	'FROZEN',
	'FINISHED',
	'SETTLED',
	'CLEARED',
	'OVERDUE',
	'BREACH',
	'TURNOUT')
and a.INVEST_ID=i.ID
and u.id=i.USERID
and  \$CONDITIONS