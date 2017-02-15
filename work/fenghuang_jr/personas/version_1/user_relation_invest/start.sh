#!/bin/sh
. /etc/profile
. ~/.bash_profile
exec_path=/root/personas_fengjr/personas/version_1/user_relation_invest
cd ${exec_path}
(
flock -w 3 200
[ $? -eq 1 ] && { echo "same one is running ----------------" ; exit 1; }
python user_relation_invest.py
)200<>./start_job.lock
