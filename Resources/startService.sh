cd /home/ec2-user/example-service
gunicorn --bind 0.0.0.0:8080 --timeout 3600 --workers 8 wsgi:app > /dev/null 2>&1 & echo $! > $1
cat $1