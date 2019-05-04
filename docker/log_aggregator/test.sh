docker-compose up -d --remove-orphans
docker-compose exec rsyslog-client sh -c 'logger "client hostname:$(hostname)"'
docker-compose exec rsyslog-client sh -c 'for level in DEBUG INFO NOTICE WARN ERR CRIT ALERT EMERG; do logger -p $level test_${level}_message; done'
docker-compose logs -f --tail=10 log-aggregator
docker-compose logs -f --tail=10 read-logs
docker-compose down
