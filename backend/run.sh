#!/bin/sh

project_home="$HOME/smartcouch"
backend="$project_home/backend"
log="$backend/log"

if [ ! -d $log ]; then
    mkdir $log
fi

python $backend/manage.py runserver 0.0.0.0:8000 >> $log/$(date '+%Y-%m-%d_%H:%M:%S').log 2>&1 &
