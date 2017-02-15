insert overwrite table app.app_user_predict_base_feature_full
select
  t.user_id,
  t.age_generation,
  t.gender_code,
  case when t.zodiac='双子座' then '1'
       when t.zodiac='处女座' then '2'
       when t.zodiac='天秤座' then '3'
       when t.zodiac='巨蟹座' then '4'
       when t.zodiac='水瓶座' then '5'
       when t.zodiac='狮子座' then '6'
       when t.zodiac='白羊座' then '7'
       when t.zodiac='金牛座' then '8'
       when t.zodiac='魔羯座' then '9'
       when t.zodiac='天蝎座' then '10'
       when t.zodiac='射手座' then '11'
       when t.zodiac='双鱼座' then '12'
  else '0' end zodiac,
  case when t.chinese_zodiac='兔' then '1'
       when t.chinese_zodiac='牛' then '2'
       when t.chinese_zodiac='狗' then '3'
       when t.chinese_zodiac='猪' then '4'
       when t.chinese_zodiac='猴' then '5'
       when t.chinese_zodiac='羊' then '6'
       when t.chinese_zodiac='虎' then '7'
       when t.chinese_zodiac='蛇' then '8'
       when t.chinese_zodiac='马' then '9'
       when t.chinese_zodiac='鸡' then '10'
       when t.chinese_zodiac='鼠' then '11'
       when t.chinese_zodiac='龙' then '12'
  else '0' end chinese_zodiac,
  t.id_card_province,
  t.id_card_city,
  case when t.mobile_province='NULL' then '0'
     when t.mobile_province='重庆' then '1'
     when t.mobile_province='浙江' then '2'
     when t.mobile_province='云南' then '3'
     when t.mobile_province='新疆' then '4'
     when t.mobile_province='西藏' then '5'
     when t.mobile_province='天津' then '6'
     when t.mobile_province='四川' then '7'
     when t.mobile_province='上海' then '8'
     when t.mobile_province='陕西' then '9'
     when t.mobile_province='山西' then '10'
     when t.mobile_province='山东' then '11'
     when t.mobile_province='青海' then '12'
     when t.mobile_province='宁夏' then '13'
     when t.mobile_province='内蒙古' then '14'
     when t.mobile_province='辽宁' then '15'
     when t.mobile_province='江西' then '16'
     when t.mobile_province='江苏' then '17'
     when t.mobile_province='吉林' then '18'
     when t.mobile_province='湖南' then '19'
     when t.mobile_province='湖北' then '20'
     when t.mobile_province='黑龙江' then '21'
     when t.mobile_province='河南' then '22'
     when t.mobile_province='河北' then '23'
     when t.mobile_province='海南' then '24'
     when t.mobile_province='贵州' then '25'
     when t.mobile_province='广西' then '26'
     when t.mobile_province='广东' then '27'
     when t.mobile_province='甘肃' then '28'
     when t.mobile_province='福建' then '29'
     when t.mobile_province='北京' then '30'
     when t.mobile_province='安徽' then '31'
     when t.mobile_province='香港' then '32'
     when t.mobile_province='澳门' then '33'
     when t.mobile_province='台湾' then '34'
 else '30' end as mobile_province,
  t.mobile_city,
 case when t.telecom_operators='电信' then '1'
      when t.telecom_operators='移动' then '2'
      when t.telecom_operators='联通' then '3'
  else '0' end as telecom_operators,
  t.is_member,
  case when t.lv_name='普通会员' then '1'
       when t.lv_name='白金用户' then '2'
       when t.lv_name='钻石用户' then '3'
       when t.lv_name='黑钻用户' then '4'
  else '0' end as lv_name,
  t1.has_bind_bank_card,
  t1.bind_bank_card_name,
  case when t2.card_value=0 then '1'
       when t2.card_value>0 and t2.card_value<10 then '2'
       when t2.card_value>=10 and t2.card_value<30 then '3'
       when t2.card_value>=30 and t2.card_value<100 then '4'
       when t2.card_value>=100 and t2.card_value<500 then '5'
       when t2.card_value>=500 then '6'
  else '0' end as card_value,
  case when t2.mobile_value>0 and t2.mobile_value<1000 then '1'
       when t2.mobile_value>=1000 and t2.mobile_value<3000 then '2'
       when t2.mobile_value>=3000 and t2.mobile_value<5000 then '3'
       when t2.mobile_value>=5000 and t2.mobile_value<10000 then '4'
       when t2.mobile_value>=10000  then '5'
  else '0' end as mobile_value,
  case when t2.mobile_phone_price>0 and t2.mobile_phone_price<500 then '1'
       when t2.mobile_phone_price>=500 and t2.mobile_phone_price<1000 then '2'
       when t2.mobile_phone_price>=1000 then '3'
  else '0' end as mobile_phone_value
from
  (
    select
        user_id,
        mobile_value,
        card_value,
        mobile_phone_price
    from
        dim.dim_user_base

  )as t2
join
  (
    select *
    from
     app.app_personas_user_base_full
    where
     dt=edw_day_amount(-1)
  )as t
on
    t2.user_id = t.user_id
join
  (
    select *
    from
      app.app_personas_user_account_full
    where
      dt=edw_day_amount(-1)
  ) as t1
on
  t2.user_id = t1.user_id
where
  t.age is not null
  and t1.is_open_ump =1
