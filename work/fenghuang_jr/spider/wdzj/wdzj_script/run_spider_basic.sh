#!/bin/sh
. /etc/profile
. ~/.bash_profile
exec_path=/data/ml/tongyang/python/spider/wdzj
cd ${exec_path}
(
flock -w 3 200 
[ $? -eq 1 ] && { echo "same one is running ----------------" ; exit 1; }
scrapy crawl basic
)200<>./start_job.lock
