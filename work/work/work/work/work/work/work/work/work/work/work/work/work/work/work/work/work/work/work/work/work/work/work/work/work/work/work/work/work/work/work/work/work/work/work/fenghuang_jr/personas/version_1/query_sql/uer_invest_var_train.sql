use crm_v2;
insert overwrite local directory '/data/ml/tongyang/test/data/invset_var'
select
 inv.USERID as user_id,
 stddev(lo.rate)
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
group by  inv.USERID