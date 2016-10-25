SELECT
	USERID as user_id,
  max(CASE WHEN type='first_no_debt' THEN times ELSE null END) as first_no_debt_time,
  max(CASE WHEN type='first_debt' THEN times ELSE null END) as first_debt_time,
  max(CASE WHEN type='last_no_debt' THEN times ELSE null END) as last_no_debt_time,
  max(CASE WHEN type='last_debt' THEN times ELSE null END) as last_debt_time,
	sum(CASE WHEN type='first_no_debt' THEN amount ELSE 0 END) as first_time_invest_amount,
	sum(CASE WHEN type='first_no_debt' THEN invest_type ELSE 0 END) as first_invest_type,
	max(CASE WHEN type='first_no_debt' THEN title ELSE null END) as first_no_debt_title,
	max(CASE WHEN type='first_debt' THEN title ELSE null END) as first_debt_title,
	sum(CASE WHEN type='last_no_debt' THEN amount ELSE 0 END) as last_no_debt_amount,
	sum(CASE WHEN type='last_debt' THEN amount ELSE 0 END) as last_debt_amount
FROM
(
SELECT 
	a.USERID,
	'first_no_debt' as type,
  a.SUBMITTIME as times,
  IF(a.CREDITASSIGNID is  NULL,1,2) as invest_type, -- 1:非债转，2：债转
	REPLACE(REPLACE(REPLACE(l.TITLE,CHAR(9),''),CHAR(10),''),CHAR(13),'') as title,
	(case when a.ORIGINALAMOUNT IS NULL THEN a.amount ELSE a.ORIGINALAMOUNT END) as amount
FROM
	TB_INVEST a
JOIN
	(
	SELECT
		USERID,
		min(case when i.CREDITASSIGNID is null then i.SUBMITTIME else null end) as no_debt_min_time
	FROM
		TB_INVEST i
	WHERE
		status in('FROZEN','FINISHED','SETTLED','CLEARED','TURNOUT','OVERDUE','BREACH')
	GROUP BY
		USERID 
	)b
ON
	a.USERID = b.USERID
LEFT OUTER JOIN
		TB_LOAN l
ON
	a.LOANID = l.ID
WHERE	
	a.SUBMITTIME = no_debt_min_time
	and a.status in('FROZEN','FINISHED','SETTLED','CLEARED','TURNOUT','OVERDUE','BREACH')


UNION ALL

SELECT 
	a.USERID,
	'first_debt' as type,
  a.SUBMITTIME as times,
	IF(a.CREDITASSIGNID is  NULL,1,2) as invest_type, -- 1:非债转，2：债转
	REPLACE(REPLACE(REPLACE(l.TITLE,CHAR(9),''),CHAR(10),''),CHAR(13),'') as title,
	a.amount as amount
FROM
	TB_INVEST a
JOIN
	(
	SELECT
		USERID,
		min(case when i.CREDITASSIGNID is not null then i.SUBMITTIME else null end) as no_debt_min_time
	FROM
		TB_INVEST i
	WHERE
		status in('FROZEN','FINISHED','SETTLED','CLEARED','TURNOUT','OVERDUE','BREACH')
	GROUP BY
		USERID 
	)b
ON
	a.USERID = b.USERID
LEFT OUTER JOIN
		TB_LOAN l
ON
	a.LOANID = l.ID
WHERE	
	a.SUBMITTIME = no_debt_min_time
	and a.status in('FROZEN','FINISHED','SETTLED','CLEARED','TURNOUT','OVERDUE','BREACH')

UNION ALL

SELECT 
	a.USERID,
	'last_no_debt' as type,
  a.SUBMITTIME as times,
  IF(a.CREDITASSIGNID is  NULL,1,2) as invest_type, -- 1:非债转，2：债转
	REPLACE(REPLACE(REPLACE(l.TITLE,CHAR(9),''),CHAR(10),''),CHAR(13),'') as title,
	(case when a.ORIGINALAMOUNT IS NULL THEN a.amount ELSE a.ORIGINALAMOUNT END) as amount
FROM
	TB_INVEST a
JOIN
	(
	SELECT
		USERID,
		max(case when i.CREDITASSIGNID is  null then i.SUBMITTIME else null end) as no_debt_min_time
	FROM
		TB_INVEST i
	WHERE
		status in('FROZEN','FINISHED','SETTLED','CLEARED','TURNOUT','OVERDUE','BREACH')
	GROUP BY
		USERID 
	)b
ON
	a.USERID = b.USERID
LEFT OUTER JOIN
		TB_LOAN l
ON
	a.LOANID = l.ID
WHERE	
	a.SUBMITTIME = no_debt_min_time
	and a.status in('FROZEN','FINISHED','SETTLED','CLEARED','TURNOUT','OVERDUE','BREACH')


UNION ALL

SELECT 
	a.user_id as userid,
	'last_debt' as type,
	a.TIMERECORDED as times,
	2 as invest_type,
	REPLACE(REPLACE(REPLACE(d.TITLE,CHAR(9),''),CHAR(10),''),CHAR(13),'') as title,
	a.amount as amount
FROM
	(
	  SELECT
	  		USER_ID AS user_id,
	  		TIMERECORDED,
	  		amount
	  FROM
			TB_FUND_RECORD
	  WHERE
			type='INVEST' and status='INITIALIZED' and operation='OUT' and realm in ('CREDITASSIGNINVEST')
	)a
JOIN
(
	SELECT
				USER_ID AS user_id,
				max(TIMERECORDED) as time_min
	FROM
				TB_FUND_RECORD
	WHERE
					type='INVEST' and status='INITIALIZED' and operation='OUT' and realm in ('CREDITASSIGNINVEST')
	GROUP BY
					USER_ID
)b
ON
	a.user_id = b.user_id
LEFT OUTER JOIN
	TB_INVEST c
ON
	a.user_id = c.userid
LEFT OUTER JOIN
	TB_LOAN d
ON
	d.ID = c.LOANID
WHERE
	a.TIMERECORDED = b.time_min
)t
where \$CONDITIONS
GROUP BY 
	userid