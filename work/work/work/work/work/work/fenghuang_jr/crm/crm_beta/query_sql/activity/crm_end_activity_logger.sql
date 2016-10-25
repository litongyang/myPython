use crm_v2;
insert overwrite local directory '/data/ml/tongyang/data/activity/activity_logger'
select
    contact_id as user_id,
    json_list(
        'activity_id',activity_id,
        'activity_type',activity_type,
        'activity_name',activity_name,
        'award_type',award_type,
        'type_id',type_id,
        'type_name',type_name,
        'correspond_id',correspond_id,
        'amount',round(amount, 2),
        'correspond_investment',round(correspond_investment, 2),
        'send_time',send_time,
        'is_send_status',is_send_status,
        'is_joined',is_joined,
        'created_user_id',created_user_id,
        'modified_user_id',modified_user_id,
        'date_entered',date_entered,
        'date_modified',date_modified,
        'deleted',deleted
      ) as activity_logger
from
    (
        select
            contact_id,
            activity_id,
            activity_type,
            activity_name,
            award_type,
            type_id,
            type_name,
            correspond_id,
            amount,
            correspond_investment,
            send_time,
            is_send_status,
            is_joined,
            created_user_id,
            modified_user_id,
            date_entered,
            date_modified,
            deleted
        from
            activity_contact_awards
        where
            is_joined='1'
            and deleted = 0
     )t
group by
    contact_id;