set hive.exec.compress.output=false;
insert overwrite local directory '/root/intelligence_info/finance/data/get_company_code' row format delimited fields terminated by '\t'

select
    s_info_windcode
from
    ods.wind_asharedescription_full
where
    dt = edw_day_amount(-1)
    and s_info_delistdate is null