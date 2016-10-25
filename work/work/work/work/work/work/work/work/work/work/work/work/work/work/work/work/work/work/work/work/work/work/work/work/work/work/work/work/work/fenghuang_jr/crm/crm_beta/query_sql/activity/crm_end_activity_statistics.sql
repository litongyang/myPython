use crm_v2;
insert overwrite local directory '/data/ml/tongyang/data/activity/activity_statistics'

select
    user_id,
    toJson(
        'activity_type',activity_type,0,
        'type_amount',type_amount,0,
        'type_cnt',type_cnt,0
    ) as activity_statistics_json
from
(
    select
        contact_id as user_id,
        activity_type,
        sum(amount) as type_amount,
        count(1) as type_cnt
    from
        activity_contact_awards
    where
        deleted = 0
        and is_joined='1'
    group by
        contact_id, activity_type
)tmp

