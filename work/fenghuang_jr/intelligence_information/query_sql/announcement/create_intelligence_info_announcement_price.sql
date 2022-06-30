create table if not exists  app.app_intelligence_info_announcement_price_full(
company_code    string,
company_name    string,
method  string,
total_count int,
announce_date string,
list_date string,
lock_date string,
type int,
pre_price_range double
suf_price_range double
)
PARTITIONED BY (dt string)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n';