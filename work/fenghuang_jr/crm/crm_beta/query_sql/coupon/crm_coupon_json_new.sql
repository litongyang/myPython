use crm_v2;

insert overwrite table crm_coupon_json_new
select
    cn.user_id,
    cn.all_count,
    cn.all_amount,
    cn.all_use_count,
    cn.accept,
    cn.accept_user_id,
    cn.send,cn.send_user_id,
    cn.register_count,
    cn.register_used,
    cn.points_count,
    cn.points_used,
    cn.rebate_count,
    cn.rebate_used,
    cn.weekend_count,
    cn.weekend_used,
    cn.newyear_count,
    cn.newyear_used,
    cn.turnplate_count,
    cn.turnplate_used,
    cn.last_new_coupon_endtime,
    toJson(
        'a',cn.all_count,0,
        'a',cn.all_amount,0,
        'a',cn.accept,0,
        'a',cn.send,0,
        'a',cn.register_count,0,
        'a',cn.register_used,0,
        'a',cn.points_count,0,
        'a',cn.points_used,0,
        'a',cn.rebate_count,0,
        'a',cn.rebate_used,0,
        'a',cn.weekend_count,0,
        'a',cn.weekend_used,0,
        'a',cn.newyear_count,0,
        'a',cn.newyear_used,0,
        'a',cn.turnplate_count,0,
        'a',cn.turnplate_used,0
        )as md5
from (
SELECT
    u.user_id as user_id,
    count(c.id) as all_count,
    sum(c.invest_amount) as all_amount,
    ((case when sum(c.register_used) is null then 0 else sum(c.register_used) end)+(case when sum(c.points_used) is null then 0 else sum(c.points_used) end)+( case when sum(c.rebate_used) is null then 0 else sum(c.rebate_used) end)
    +(case when sum(c.weekend_used) is null then 0 else sum(c.weekend_used) end)+(case when sum(c.newyear_used) is null then 0 else sum(c.newyear_used) end)+(case when sum(c.turnplate_used) is null then 0 else sum(c.turnplate_used) end))
    as all_use_count,
    case when max(t.accept) is null then 0 else max(t.accept) end as accept,
    case when max(r.send) is null then 0 else max(r.send) end as send,
    case when sum(c.register_count) is null then 0 else sum(c.register_count) end  as register_count,
    case when sum(c.register_used) is null then 0 else sum(c.register_used) end as register_used,
    case when sum(c.points_count) is null then 0 else sum(c.points_count) end as points_count,
    case when sum(c.points_used) is null then 0 else sum(c.points_used) end as points_used,
    case when sum(c.rebate_count) is null then 0 else sum(c.rebate_count) end as rebate_count,
    case when sum(c.rebate_used) is null then 0 else sum(c.rebate_used) end as rebate_used,
    case when sum(c.weekend_count) is null then 0 else sum(c.weekend_count) end as weekend_count,
    case when sum(c.weekend_used) is null then 0 else sum(c.weekend_used) end as weekend_used,
    case when sum(c.newyear_count) is null then 0 else sum(c.newyear_count) end as newyear_count,
    case when sum(c.newyear_used) is null then 0 else sum(c.newyear_used) end as newyear_used,
    case when sum(c.turnplate_count) is null then 0 else  sum(c.turnplate_count) end as turnplate_count,
    case when sum(c.turnplate_used) is null then 0 else sum(c.turnplate_used) end as turnplate_used,
    max(case when c.tag='register'then endtime else null end) as last_new_coupon_endtime,
    max(t.ids) as accept_user_id,
    max(r.ids) as send_user_id
FROM
        common.user_static u left JOIN
        (
                SELECT
                        r.*,
                        CASE
                WHEN i.ORIGINALAMOUNT IS NULL THEN
                        i.amount
                ELSE
                        i.ORIGINALAMOUNT
                END AS invest_amount
                FROM
                        tb_coupon_record_crm r
                LEFT JOIN tb_invest i ON r.ENTITYID = i.ID where r.tag <> 'other'
        ) AS c on
        u.user_id = c.USERID LEFT JOIN (select USERID, count(id) as accept,concat_ws(',', collect_set(REF_ID)) as ids from tb_invite_reward_trace  group by USERID ) as t on u.user_id = t.USERID
    LEFT JOIN (select REF_ID , count(id) as send,concat_ws(',', collect_set(USERID)) as ids from tb_invite_reward_trace  group by REF_ID ) as r on u.user_id =r.REF_ID
        where c.USERid IS NOT NULL OR T.USERID IS NOT NULL OR R.REF_ID IS NOT NULL
GROUP BY
        u.user_id
 ) as cn;