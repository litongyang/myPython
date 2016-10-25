use crm_v2;
insert overwrite local directory '/data/ml/tongyang/data/coupon/coupon_statistics'
select
    c.user_id,
    toJson(
        'all_count',c.all_count,0,
        'all_amount',c.all_amount,0,
        'all_use_count',c.all_use_count,0,
        'avg_amount',int(c.all_amount/c.all_use_count),0,
        'accept',c.accept,0,
        'accept_user_id',c.accept_user_id,0,
        'send',c.send,0,
        'send_user_id',c.send_user_id,0,
        'register_count',c.register_count,0,
        'register_used', c.register_used,0,
        'points_count',c.points_count,0,
        'points_used',c.points_used,0,
        'rebate_count',c.rebate_count,0,
        'rebate_used',c.rebate_used,0,
        'weekend_count',c.weekend_count,0,
        'weekend_used',c.weekend_used,0,
        'newyear_count',c.newyear_count,0,
        'newyear_used',c.newyear_used,0,
        'turnplate_count',c.turnplate_count,0,
        'turnplate_used',c.turnplate_used,0,
        'last_new_coupon_endtime',c.last_new_coupon_endtime,0
     ) as coupon_static_json
from
    crm_coupon_json_new as c;