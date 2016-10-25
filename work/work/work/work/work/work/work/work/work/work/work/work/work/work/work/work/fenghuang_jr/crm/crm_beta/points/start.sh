#!/bin/sh
. /etc/profile
. ~/.bash_profile
exec_path=/data/ml/tongyang/python/work/fenghuang_jr/crm/crm_beta/points
cd ${exec_path}
(
flock -w 3 200 
[ $? -eq 1 ] && { echo "same one is running ----------------" ; exit 1; }
python start_points.py
)200<>./start_job.lock