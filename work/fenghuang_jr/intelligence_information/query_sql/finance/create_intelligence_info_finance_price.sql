create table if not exists  app.app_intelligence_info_finance_price_full(
company_code    string,
type int,
finance_date string,
price_range double
)
PARTITIONED BY (dt string)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n';