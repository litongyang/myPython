set hive.exec.compress.output=false;
insert overwrite local directory '/root/intelligence_info/announcement/data/get_prices_all' row format delimited fields terminated by '\t'
select
    t.wind_code,
    t.s_dq_close,
    case when t.trade_dt is null then t.ann_dt
    else t.trade_dt end as trade_date,
    t.ann_dt,
    t.report_period,
    case when substr(report_period,5,2)='03' then 'Q1'
                 when substr(report_period,5,2)='06' then 'Q2'
                 when substr(report_period,5,2)='09' then 'Q3'
                 when substr(report_period,5,2)='12' then 'year'
            else '' end as type,
    substr(report_period,0,4) as years
from
(
    select
        a.wind_code,
        b.s_dq_close,
        b.trade_dt,
        a.ann_dt,
        a.report_period
    from
    (
        select
            wind_code,
            report_period,
            ann_dt
        from
            ods.wind_ashareincome_full
        where
            statement_type='408001000'
            and dt = edw_day_amount(-1)
        group by
            wind_code,
            ann_dt,
            report_period
    )a
    left outer join
    (
        select
          s_info_windcode as wind_code,
          s_dq_close,
          trade_dt
        from
            ods.wind_ashareeodprices_full
        where
            dt = edw_day_amount(-1)
    )b
    on
         a.wind_code = b.wind_code
         and a.ann_dt = b.trade_dt
    union all
    select
        a.wind_code,
        a.s_dq_close,
        a.trade_dt,
        b.ann_dt,
        b.report_period
    from
    (
        select
          s_info_windcode as wind_code,
          s_dq_close,
          trade_dt
        from
            ods.wind_ashareeodprices_full
        where
            dt = edw_day_amount(-1)
        order by wind_code, trade_dt
    )a
    left outer join
    (
        select
            wind_code,
            report_period,
            ann_dt
        from
            ods.wind_ashareincome_full
        where
            statement_type='408001000'
            and dt = edw_day_amount(-1)
        group by
            wind_code,
            ann_dt,
            report_period
    )b
    on
        a.wind_code = b.wind_code
        and a.trade_dt = b.ann_dt
)t
order by
    t.wind_code,
    trade_date
