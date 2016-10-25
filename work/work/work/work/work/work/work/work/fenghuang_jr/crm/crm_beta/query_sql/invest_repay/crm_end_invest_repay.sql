use crm_v2;
insert overwrite local directory '/data/ml/tongyang/data/invest_repay/invest_repay_logger'
select
    user_id,
    json_list(
        'currentperiod',currentperiod,
        'repay_date',repay_date,
        'repay_amount',repay_amount
    ) as invest_repay_logger
from
    invest_repay_logger
group by
    user_id;