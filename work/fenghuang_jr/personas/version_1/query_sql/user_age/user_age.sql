use common;
insert overwrite local directory '/data/ml/tongyang/test/data/user_age'
select
  user_id,
  age
from
  user_static
where
  age is not null
