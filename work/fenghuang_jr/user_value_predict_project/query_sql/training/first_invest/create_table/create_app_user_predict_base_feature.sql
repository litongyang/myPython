create table if not exists  app.app_user_predict_base_feature_full(
user_id           string,
age_generation    string,
gender_code       string,
zodiac            string,
chinese_zodiac    string,
id_card_province  string,
id_card_city      string,
mobile_province   string,
mobile_city       string,
telecom_operators string,
is_member         string,
lv_name           string,
has_bind_bank_card string,
bind_bank_card_name string,
card_value        string,
mobile_value      string,
mobile_phone_value string
) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n';
