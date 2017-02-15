set hive.exec.compress.output=false;
insert overwrite local directory '/root/personas_fengjr/data/user_age' row format delimited fields terminated by '\t'
select
  user_id,
  age
from
  dim.dim_user_base
where
  age is not null
