#! /bin/bash
#export /home/taiga/venvs/taiga/bin/python='/home/taiga/venvs/taiga/bin/python3'
cd /home/taiga/taiga-back-stable/
/home/taiga/venvs/taiga/bin/python manage.py migrate --noinput
/home/taiga/venvs/taiga/bin/python manage.py loaddata initial_user
/home/taiga/venvs/taiga/bin/python manage.py loaddata initial_project_templates
/home/taiga/venvs/taiga/bin/python manage.py compilemessages
/home/taiga/venvs/taiga/bin/python manage.py collectstatic --noinput
# option load sample_data
HOSTNAME=$(hostname)
if [ "$HOSTNAME" = "server3" ]; then
    echo "This server is ${HOSTNAME}, Waitting...load  taiga sample_data"
    cd /home/taiga/taiga-back-stable/
    /home/taiga/venvs/taiga/bin/python manage.py sample_data
fi
#/home/taiga/venvs/taiga/bin/python manage.py runserver 0.0.0.0:8000
