load data local inpath '/root/intelligence_info/announcement/result/finance/announcement_result.txt' overwrite into table app.app_intelligence_info_announcement_price_full partition(dt='${dt}');