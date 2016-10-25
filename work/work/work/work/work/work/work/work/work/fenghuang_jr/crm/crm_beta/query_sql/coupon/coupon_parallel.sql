use crm_v2;
insert overwrite table coupon_record_crm_invest
SELECT
    i.id,
    r.ENTITYID,
    r.coupon_id,
    r.couponname,
    r.USERID,
    r.timecreated,
    i.SUBMITTIME,
    case when i.ORIGINALAMOUNT is null then i.amount else i.ORIGINALAMOUNT end as AMOUNT,
    r.tag
FROM
    tb_coupon_record_crm r
left outer join
    tb_invest i
on
    r.ENTITYID = i.ID;




insert overwrite table crm_coupon_json_diff
select
    e.user_id,
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
        'logger',e.logger,1)
from
 (
    select
    b.user_id,
    json_list(
        'invest_id',a.invest_id,
        'is_used',case when a.invest_id is null then 0 else 1 end,
        'coupon_id',a.coupon_id,
        'amount',a.amount,
        'tag',a.tag,
        'coupon_name',a.couponname,
        'created_time',substr(a.timecreated,1,10),
        'created_time_int',int(regexp_replace(substr(a.timecreated,1,10),'[-]','')),
        'submit_time',substr(a.submittime,1,10),
        'submit_time_int',int(regexp_replace(substr(a.submittime,1,10),'[-]',''))) as logger
    from
    (
        select
            user_id
        from
        (
            select
                user_id
            from
                coupon_record_crm_invest
         ) as a
        group by a.user_id
    ) as b
    left outer join
        coupon_record_crm_invest as a
    on
        a.user_id = b.user_id
    group by b.user_id
 ) as e
left outer join
    crm_coupon_json_new as c
 on
    e.user_id=c.user_id;




--�����ǩ
--insert overwrite table crm_coupon_json_new
--select
--    cn.user_id,
--    cn.all_count,
--    cn.all_amount,
--    cn.all_use_count,
--    cn.accept,
--    cn.accept_user_id,
--    cn.send,cn.send_user_id,
--    cn.register_count,
--    cn.register_used,
--    cn.points_count,
--    cn.points_used,
--    cn.rebate_count,
--    cn.rebate_used,
--    cn.weekend_count,
--    cn.weekend_used,
--    cn.newyear_count,
--    cn.newyear_used,
--    cn.turnplate_count,
--    cn.turnplate_used,
--    toJson(
--        'a',cn.all_count,0,
--        'a',cn.all_amount,0,
--        'a',cn.accept,0,
--        'a',cn.send,0,
--        'a',cn.register_count,0,
--        'a',cn.register_used,0,
--        'a',cn.points_count,0,
--        'a',cn.points_used,0,
--        'a',cn.rebate_count,0,
--        'a',cn.rebate_used,0,
--        'a',cn.weekend_count,0,
--        'a',cn.weekend_used,0,
--        'a',cn.newyear_count,0,
--        'a',cn.newyear_used,0,
--        'a',cn.turnplate_count,0,
--        'a',cn.turnplate_used,0
--        )as md5
--from (
--SELECT
--    u.user_id as user_id,
--    count(c.id) as all_count,
--    sum(c.invest_amount) as all_amount,
--    ((case when sum(c.register_used) is null then 0 else sum(c.register_used) end)+(case when sum(c.points_used) is null then 0 else sum(c.points_used) end)+( case when sum(c.rebate_used) is null then 0 else sum(c.rebate_used) end)
--    +(case when sum(c.weekend_used) is null then 0 else sum(c.weekend_used) end)+(case when sum(c.newyear_used) is null then 0 else sum(c.newyear_used) end)+(case when sum(c.turnplate_used) is null then 0 else sum(c.turnplate_used) end))
--    as all_use_count,
--    case when max(t.accept) is null then 0 else max(t.accept) end as accept,
--    case when max(r.send) is null then 0 else max(r.send) end as send,
--    case when sum(c.register_count) is null then 0 else sum(c.register_count) end  as register_count,
--    case when sum(c.register_used) is null then 0 else sum(c.register_used) end as register_used,
--    case when sum(c.points_count) is null then 0 else sum(c.points_count) end as points_count,
--    case when sum(c.points_used) is null then 0 else sum(c.points_used) end as points_used,
--    case when sum(c.rebate_count) is null then 0 else sum(c.rebate_count) end as rebate_count,
--    case when sum(c.rebate_used) is null then 0 else sum(c.rebate_used) end as rebate_used,
--    case when sum(c.weekend_count) is null then 0 else sum(c.weekend_count) end as weekend_count,
--    case when sum(c.weekend_used) is null then 0 else sum(c.weekend_used) end as weekend_used,
--    case when sum(c.newyear_count) is null then 0 else sum(c.newyear_count) end as newyear_count,
--    case when sum(c.newyear_used) is null then 0 else sum(c.newyear_used) end as newyear_used,
--    case when sum(c.turnplate_count) is null then 0 else  sum(c.turnplate_count) end as turnplate_count,
--    case when sum(c.turnplate_used) is null then 0 else sum(c.turnplate_used) end as turnplate_used,
--    max(t.ids) as accept_user_id,
--    max(r.ids) as send_user_id
--FROM
--        common.user_static u left JOIN
--        (
--                SELECT
--                        r.*,
--                        CASE
--                WHEN i.ORIGINALAMOUNT IS NULL THEN
--                        i.amount
--                ELSE
--                        i.ORIGINALAMOUNT
--                END AS invest_amount
--                FROM
--                        tb_coupon_record_crm r
--                LEFT JOIN tb_invest i ON r.ENTITYID = i.ID where r.tag <> 'other'
--        ) AS c on
--        u.user_id = c.USERID LEFT JOIN (select USERID, count(id) as accept,concat_ws(',', collect_set(REF_ID)) as ids from tb_invite_reward_trace  group by USERID ) as t on u.user_id = t.USERID
--    LEFT JOIN (select REF_ID , count(id) as send,concat_ws(',', collect_set(USERID)) as ids from tb_invite_reward_trace  group by REF_ID ) as r on u.user_id =r.REF_ID
--        where c.USERid IS NOT NULL OR T.USERID IS NOT NULL OR R.REF_ID IS NOT NULL
--GROUP BY
--        u.user_id) as cn;