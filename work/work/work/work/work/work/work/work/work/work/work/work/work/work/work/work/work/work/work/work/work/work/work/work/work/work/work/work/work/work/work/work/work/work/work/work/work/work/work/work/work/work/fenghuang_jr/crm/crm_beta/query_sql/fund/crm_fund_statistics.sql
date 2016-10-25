use crm_v2;
insert overwrite table crm_fund_statistics
SELECT
	t.user_id,
	t.balance_amount,
	t.total_amount,
	t.available_amount,
	c.first_deposit_date,
	c.first_withdraw_date,
	c.last_withdraw_date
FROM
(
	SELECT
		a.USERID as user_id,
		a.balance_amount,
		sum(a.balance_amount + if(b.amountinterest is not null,b.amountinterest,0)+ if(b.amountprincipal is not null, b.amountprincipal,0)) as total_amount,
		-- sum(CASE WHEN a.update_last = b.DUEDATE THEN a.balance_amount+b.amountinterest+b.amountprincipal ELSE a.balance_amount end) as total_amount,
		a.available_amount
	FROM
	(
		SELECT
			USERID,
			TIMELASTUPDATED,
			sum(AVAILABLE_AMOUNT)+sum(FROZEN_AMOUNT) as balance_amount,
			sum(AVAILABLE_AMOUNT)as available_amount
		FROM
			TB_USER_FUND
		GROUP BY
			USERID,TIMELASTUPDATED
	)a
	left outer JOIN
		(
			SELECT
				a.USERID as USERID,
				sum(b.amountinterest) as amountinterest,
				sum(b.amountprincipal) as amountprincipal
			FROM
				TB_INVEST a
			JOIN
				TB_INVEST_REPAYMENT b
			ON
				a.id = b.INVEST_ID
			WHERE
				b.status in ('UNDUE','OVERDUE','BREACHE')
			GROUP BY
				a.USERID
		)b
	ON
		a.USERID = b.USERID
	group by a.USERID,a.balance_amount,a.available_amount
)t
left outer join
	(
		select
			user_id,
			min(case when type=0 then date else null end) as first_deposit_date,
			min(case when type=1 then date else null end) as first_withdraw_date,
			max(case when type=1 then date else null end) as last_withdraw_date
		from
			crm_fund_logger
		group by
			user_id
	)c
on
	t.user_id = c.user_id;

