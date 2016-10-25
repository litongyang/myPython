use crm_v2;
insert overwrite table crm_fund_logger
SELECT
		USER_ID as user_id,
		'0' as type,
		'deposit' as type_name,
		AMOUNT as amount,
		regexp_replace(substr(timerecorded,1,10),'[-]','') as date
FROM
	TB_FUND_RECORD
WHERE
	operation = 'IN'
	and status='SUCCESSFUL'
	and type='DEPOSIT'

union all

SELECT
		USER_ID as user_id,
		'1' as type,
		'withdraw' as type_name,
		AMOUNT as amount,
		regexp_replace(substr(timerecorded,1,10),'[-]','') as date
FROM
	TB_FUND_RECORD
WHERE
	operation = 'OUT'
	and status='SUCCESSFUL'
	and type='WITHDRAW'

--UNION ALL
--
--SELECT
--		USER_ID as user_id,
--		'2' as type,
--		'payment' as type_name,
--		AMOUNT as amount,
--		regexp_replace(substr(timerecorded,1,10),'[-]','') as date
--FROM
--	TB_FUND_RECORD
--WHERE
--	operation = 'IN'
--	and status='SUCCESSFUL'
--	and type='INVEST_REPAY'



--SELECT
--	a.USERID as user_id,
--	'2' as type,
--	'payment' as type_name,
--	b.repay_amount as amount,
--	b.repay_date as date
--FROM
--	TB_INVEST a
--JOIN
--(
--	SELECT
--		INVEST_ID,
--		MAX(duedate) as repay_date,
--		sum(AMOUNTINTEREST)+sum(AMOUNTPRINCIPAL) as repay_amount
--	FROM
--		TB_INVEST_REPAYMENT
--	GROUP BY
--		INVEST_ID
--)b
--ON
--	a.ID = b.INVEST_ID
