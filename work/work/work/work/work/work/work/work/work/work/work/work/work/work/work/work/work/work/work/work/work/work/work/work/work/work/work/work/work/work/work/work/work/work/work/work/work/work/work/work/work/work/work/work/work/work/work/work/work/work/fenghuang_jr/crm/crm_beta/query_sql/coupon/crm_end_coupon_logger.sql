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


insert overwrite local directory '/data/ml/tongyang/data/coupon/coupon_logger'
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
    group by b.user_id;