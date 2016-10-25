use crm_v2;
insert overwrite local directory '/data/ml/tongyang/data/fund/fund_statistics'

select
    user_id,
    toJson(
        'balance_amount',round(balance_amount,2),0,
        'total_amount',round(total_amount,2),0,
        'available_amount',round(available_amount,2),0,
        'first_deposit_date',first_deposit_date,0,
        'first_withdraw_date',first_withdraw_date,0,
        'last_withdraw_date',last_withdraw_date,0
    ) as fund_statistics_json
from
    crm_fund_statistics
