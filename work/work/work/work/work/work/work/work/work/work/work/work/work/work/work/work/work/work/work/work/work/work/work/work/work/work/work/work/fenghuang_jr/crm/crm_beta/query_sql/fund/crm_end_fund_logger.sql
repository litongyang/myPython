use crm_v2;
insert overwrite local directory '/data/ml/tongyang/data/fund/fund_logger'

select
    user_id,
    json_list(
        'type',type,
        'type_name',type_name,
        'amount',round(amount,2),
        'date',date
    ) as fund_logger_list
from
    crm_fund_logger
group by
    user_id;