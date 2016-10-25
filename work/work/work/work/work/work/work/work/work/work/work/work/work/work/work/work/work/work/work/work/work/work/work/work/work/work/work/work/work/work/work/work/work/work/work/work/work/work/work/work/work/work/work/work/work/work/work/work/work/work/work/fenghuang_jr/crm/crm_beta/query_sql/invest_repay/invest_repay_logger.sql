SELECT
    b.USERID as user_id,
    a.CURRENTPERIOD,
    a.DUEDATE as repay_date,
    a.AMOUNTINTEREST + a.AMOUNTPRINCIPAL  as repay_amount
FROM
    TB_INVEST as b,
    TB_INVEST_REPAYMENT as a
where
    b.ID=a.INVEST_ID
    and a.STATUS <> 'COLLECTED'
    and  \$CONDITIONS