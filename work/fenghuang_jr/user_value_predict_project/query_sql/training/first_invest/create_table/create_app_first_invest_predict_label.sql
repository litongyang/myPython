create table if not exists  app.app_user_predict_first_invest_label(
user_id    string,
y_1_amount double,
y_2_amount double,
y_3_amount double,
y_6_amount double,
y_9_amount double,
y_12_amount double
) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n';

